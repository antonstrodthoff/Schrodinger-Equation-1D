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

rd.load_data("schrodinger.inp")
MASS = rd.particle_mass()
X_MIN = rd.x_minimum()
X_MAX = rd.x_maximum()
NPOINT = rd.n_point()
FVAL = rd.first_eigenvalue()
LVAL = rd.last_eigenvalue()
INTER_TYPE = rd.interpolation_type()
X_POT = rd.x_potential()
Y_POT = rd.y_potential()
DELTA = (X_MAX-X_MIN)/NPOINT
CONST_A = 1/(MASS*DELTA**2)
X_AXIS = np.linspace(X_MIN, X_MAX, NPOINT)

def norm(vector):
    """
    Docstring
    """
    ss = 0
    for element in vector:
        ss += element**2
    return (ss*DELTA)**(1/2)

def normalize(vector):
    """
    Docstring
    """
    factor = norm(vector)
    for (index, _) in enumerate(vector):
        vector[index] /= factor
    return vector

def exp_x(vector):
    """
    Docstring
    """
    ss = 0
    for (index, element) in enumerate(vector):
        ss += X_AXIS[index]*element**2
    return DELTA*ss

def exp_x_sqrd(vector):
    """
    Docstring
    """
    ss = 0
    for (index, element) in enumerate(vector):
        ss += X_AXIS[index]**2*element**2
    return DELTA*ss

def uncertainty(vector):
    """
    Docstring
    """
    return (exp_x_sqrd(vector)-exp_x(vector)**2)**(1/2)

def calculate_and_save_results():
    """
    Docstring
    """
    #interpolating
    y_pot_inter = []
    if INTER_TYPE == "polynomial":
        y_pot_inter = KroghInterpolator(X_POT, Y_POT)
    else:
        y_pot_inter = interp1d(X_POT, Y_POT, kind=INTER_TYPE)

    #calculating
    expected_x = np.array([])
    uncertainties = np.array([])
    energies = np.array([])
    norm_eigenvecs = np.array([])
    maindiag = y_pot_inter(X_AXIS)+CONST_A
    seconddiag = np.full(NPOINT-1, -1/2*CONST_A)
    selectrange = (FVAL-1, LVAL-1)
    ev = eigh_tridiagonal(maindiag, seconddiag, select="i", select_range=selectrange)
    (energies, eigenvecs) = ev
    norm_eigenvecs = np.array([normalize(eigenvec) for eigenvec in eigenvecs.T])
    expected_x = np.array([exp_x(eigenvec) for eigenvec in norm_eigenvecs])
    uncertaintylist = [uncertainty(eigenvec) for eigenvec in norm_eigenvecs]
    uncertainties = np.array(uncertaintylist)

    #saving
    rd.save_xyformat("potential.dat", X_AXIS, y_pot_inter(X_AXIS))
    rd.save_nxyformat("wavefuncs.dat", X_AXIS, norm_eigenvecs.T)
    rd.save_xyformat("energies.dat", energies, ["" for _ in energies])
    rd.save_xyformat("expvalues.dat", expected_x, uncertainties)

    #plotting
    plt.plot(X_AXIS, y_pot_inter(X_AXIS))
    plt.plot(X_AXIS, norm_eigenvecs[3])
    plt.show()
