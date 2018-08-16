#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:41:54 2018

@author: Anton
"""

import readdata as rd
import numpy as np
from scipy.interpolate import interp1d, KroghInterpolator
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

class Eigensolver:
    """
    Docstring
    """
    reader = rd.Datareader()
    mass = reader.particle_mass()
    x_min = reader.x_minimum()
    x_max = reader.x_maximum()
    npoint = reader.n_point()
    fval = reader.first_eigenvalue()
    lval = reader.last_eigenvalue()
    inter_type = reader.interpolation_type()
    inter_points = reader.interpolation_points()
    x_pot = reader.x_potential()
    y_pot = reader.y_potential()
    delta = (x_max-x_min)/npoint
    const_a = 1/(mass*delta**2)
    x_axis = np.linspace(x_min, x_max, npoint)
    y_pot_inter = []
    energies = np.array([])
    norm_eigenvecs = np.array([])
    expected_x = np.array([])
    uncertainties = np.array([])

    def norm(self, vector):
        """
        Docstring
        """
        ss = 0
        for element in vector:
            ss += element**2
        return (ss*self.delta)**(1/2)

    def normalize(self, vector):
        """
        Docstring
        """
        factor = self.norm(vector)
        for (index, _) in enumerate(vector):
            vector[index] /= factor
        return vector

    def exp_x(self, vector):
        """
        Docstring
        """
        ss = 0
        for (index, element) in enumerate(vector):
            ss += self.x_axis[index]*element**2
        return self.delta*ss

    def exp_x_sqrd(self, vector):
        """
        Docstring
        """
        ss = 0
        for (index, element) in enumerate(vector):
            ss += self.x_axis[index]**2*element**2
        return self.delta*ss

    def uncertainty(self, vector):
        """
        Docstring
        """
        return (self.exp_x_sqrd(vector)-self.exp_x(vector)**2)**(1/2)

    def interpolate(self):
        """
        Docstring
        """
        if self.inter_type == "polynomial":
            self.y_pot_inter = KroghInterpolator(self.x_pot, self.y_pot)
        else:
            self.y_pot_inter = interp1d(self.x_pot, self.y_pot, kind=self.inter_type)

    def calculate_results(self):
        """
        Docstring
        """
        maindiag = self.y_pot_inter(self.x_axis)+self.const_a
        seconddiag = np.full(self.npoint-1, -1/2*self.const_a)
        selectrange = (self.fval-1, self.lval-1)
        ev = eigh_tridiagonal(maindiag, seconddiag, select="i", select_range=selectrange)
        (self.energies, eigenvecs) = ev
        self.norm_eigenvecs = np.array([self.normalize(eigenvec) for eigenvec in eigenvecs.T])
        self.expected_x = np.array([self.exp_x(eigenvec) for eigenvec in self.norm_eigenvecs])
        uncertaintylist = [self.uncertainty(eigenvec) for eigenvec in self.norm_eigenvecs]
        self.uncertainties = np.array(uncertaintylist)

    def save_results(self):
        """
        Docstring
        """
        rd.save_xyformat("potential.dat", self.x_axis, self.y_pot_inter(self.x_axis))
        rd.save_nxyformat("wavefuncs.dat", self.x_axis, self.norm_eigenvecs.T)
        rd.save_xyformat("energies.dat", self.energies, ["" for _ in self.energies])
        rd.save_xyformat("expvalues.dat", self.expected_x, self.uncertainties)

    def plot(self, num):
        """
        Docstring
        """
        plt.plot(self.x_axis, self.norm_eigenvecs[num])
        plt.plot(self.x_axis, self.y_pot_inter(self.x_axis))
        plt.show()
