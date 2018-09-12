#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:41:54 2018

@author: Anton
"""

import numpy as np
from scipy.interpolate import interp1d, KroghInterpolator
from scipy.linalg import eigh_tridiagonal
import readdata as rd

def norm(vector, delta):
    """
    calculates the norm of a vector

    :type vector: nparray
    :param vector: vector to calculate the norm of

    :type delta: float
    :param delta: spacing of the vector entries on the x-axis

    :rtype: float
    :returns: the norm of the vector
    """
    ss = 0
    for element in vector:
        ss += element**2
    return (ss*delta)**(1/2)

def normalize(vector, delta):
    """
    normalizes a vector

    :type vector: nparray
    :param vector: vector to be normalized

    :type delta: float
    :param delta: spacing of the vector entries on the x-axis

    :rtype: nparray
    :returns: a normalized version of the vector
    """
    factor = norm(vector, delta)
    for (index, _) in enumerate(vector):
        vector[index] /= factor
    return vector

def exp_x(vector, delta, x_axis):
    """
    calculates the expected value of the location x of a vector

    :type vector: nparray
    :param vector: vector the expected value will be calculated of

    :type delta: float
    :param delta: spacing of the vector entries on the x-axis

    :type x_axis: nparray
    :param x_axis: the points on the x axis where the vector is defined

    :rtype: float
    :returns: the expected value of the location
    """
    ss = 0
    for (index, element) in enumerate(vector):
        ss += x_axis[index]*element**2
    return delta*ss

def exp_x_sqrd(vector, delta, x_axis):
    """
    calculates the expected value of the square of the location x of a vector

    :type vector: nparray
    :param vector: vector the expected value will be calculated of

    :type delta: float
    :param delta: spacing of the vector entries on the x-axis

    :type x_axis: nparray
    :param x_axis: the points on the x axis where the vector is defined

    :rtype: float
    :returns: the expected value of the squared location
    """
    ss = 0
    for (index, element) in enumerate(vector):
        ss += x_axis[index]**2*element**2
    return delta*ss

def uncertainty(vector, delta, x_axis):
    """
    calculates the uncertainty in position of a particle

    :type vector: nparray
    :param vector: vector the uncertainty will be calculated of

    :type delta: float
    :param delta: spacing of the vector entries on the x-axis

    :type x_axis: nparray
    :param x_axis: the points on the x axis where the vector is defined

    :rtype: float
    :returns: the uncertainty in position
    """
    return (exp_x_sqrd(vector, delta, x_axis)-exp_x(vector, delta, x_axis)**2)**(1/2)

def calculate_and_save_results(inputpath, outputpath):
    """
    this function does three things:
        -interpolating the given points of the potential defined by the user
        -solving the schrodinger equation and calculating the eigenstates,
    eigenvalues, expected values and uncertainties
        -saving the results in .dat files

    :type inputpath: string
    :param inputpath: path of the schrodinger.inp file containing the input information

    :type outputpath: string
    :param outputpath: path of the directory the .dat files will be stored in
    """
    rd.load_data(inputpath)
    mass = rd.particle_mass()
    x_min = rd.x_minimum()
    x_max = rd.x_maximum()
    npoint = rd.n_point()
    fval = rd.first_eigenvalue()
    lval = rd.last_eigenvalue()
    inter_type = rd.interpolation_type()
    x_pot = rd.x_potential()
    y_pot = rd.y_potential()
    delta = (x_max-x_min)/npoint
    const_a = 1/(mass*delta**2)
    x_axis = np.linspace(x_min, x_max, npoint)
    y_pot_inter = []
    expected_x = np.array([])
    uncertainties = np.array([])
    energies = np.array([])
    norm_eigenvecs = np.array([])

    #interpolating
    if inter_type == "polynomial":
        y_pot_inter = KroghInterpolator(x_pot, y_pot)
    else:
        y_pot_inter = interp1d(x_pot, y_pot, kind=inter_type)

    #calculating
    maindiag = y_pot_inter(x_axis)+const_a
    seconddiag = np.full(npoint-1, -1/2*const_a)
    selectrange = (fval-1, lval-1)
    ev = eigh_tridiagonal(maindiag, seconddiag, select="i", select_range=selectrange)
    (energies, eigenvecs) = ev
    norm_eigenvecs = np.array([normalize(eigenvec, delta) for eigenvec in eigenvecs.T])
    expected_x = np.array([exp_x(eigenvec, delta, x_axis) for eigenvec in norm_eigenvecs])
    uncertaintylist = [uncertainty(eigenvec, delta, x_axis) for eigenvec in norm_eigenvecs]
    uncertainties = np.array(uncertaintylist)

    #saving
    if not outputpath.endswith("/"):
        outputpath = outputpath + "/"
    rd.save_xyformat(outputpath + "potential.dat", x_axis, y_pot_inter(x_axis))
    rd.save_nxyformat(outputpath + "wavefuncs.dat", x_axis, norm_eigenvecs.T)
    rd.save_xyformat(outputpath + "energies.dat", energies, ["" for _ in energies])
    rd.save_xyformat(outputpath + "expvalues.dat", expected_x, uncertainties)

    print("The results have been saved succesfully into the folder \"" + outputpath + "\".")
