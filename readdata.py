#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:27:16 2018

@author: Anton
"""

import numpy as np

SPECIFICATIONS = []

def load_data(inputpath):
    """
    loads the data from the input file

    :type inputpath: string
    :param inputpath: path of the schrodinger.inp file containing the input information
    """
    with open(inputpath, "r") as datafile:
        data = datafile.read()

    #extracts the information by splitting the string of the input file.
    data = data.replace("\n", " ")
    data = data.replace("\t", " ")
    data = data.split(" ")

    SPECIFICATIONS.clear()

    for string in data:
        if string == "linear" or string == "polynomial":
            SPECIFICATIONS.append(string)
        elif string == "cspline":
            SPECIFICATIONS.append("cubic")
        try:
            SPECIFICATIONS.append(float(string))
        except ValueError:
            continue

def particle_mass():
    """
    returns the mass of the particle

    :rtype: float
    :returns: mass of the particle
    """
    return SPECIFICATIONS[0]

def x_minimum():
    """
    returns the lower bound of the interval, the SE has to be solved in

    :rtype: float
    :returns: lower bound of interval
    """
    return SPECIFICATIONS[1]

def x_maximum():
    """
    returns the upper bound of the interval, the SE has to be solved in

    :rtype: float
    :returns: upper bound of interval
    """
    return SPECIFICATIONS[2]

def n_point():
    """
    returns the number of interpolation points of the potential

    :rtype: float
    :returns: number of interpolation points
    """
    return int(SPECIFICATIONS[3])

def first_eigenvalue():
    """
    returns the index of the first eigenvalue to be calculated

    :rtype: float
    :returns: first eigenvalue to be calculated
    """
    return int(SPECIFICATIONS[4])

def last_eigenvalue():
    """
    returns the index of the last eigenvalue to be calculated

    :rtype: float
    :returns: last eigenvalue to be calculated
    """
    return int(SPECIFICATIONS[5])

def interpolation_type():
    """
    returns the interpolation type of the potential

    :rtype: string
    :returns: interpolation type (linear, cubic or polynomial)
    """
    return SPECIFICATIONS[6]

def interpolation_points():
    """
    returns the number of interpolation points specified by the user

    :rtype: float
    :returns: number of interpolation points
    """
    return SPECIFICATIONS[7]

def x_potential():
    """
    returns an array of the x values of the potential given by the user

    :rtype: float
    :returns: the x values of the user specified potential
    """
    x_pot = np.array(SPECIFICATIONS[8:len(SPECIFICATIONS):2])
    return x_pot

def y_potential():
    """
    returns an array of the y values of the potential given by the user

    :rtype: float
    :returns: the y values of the user specified potential
    """
    return np.array(SPECIFICATIONS[9:len(SPECIFICATIONS):2])

def read_xyformat(filename):
    """
    can be used to read information from files in the X-Y-format and N-X-Y-format
    returns an array of the information

    :type filename: string
    :param filename: name of the file to be read

    :rtype: nparray
    :returns: a 2xN array containing the information
    """
    datalist = []
    with open(filename, "r") as datafile:
        data = datafile.read()
        data = data.split("\n")
        for element in data:
            datalist.append(list(map(float, element.split(" "))))
    return np.array(datalist).T

def save_xyformat(filename, xx, yy):
    """
    can be used to save an array of format 2xN into a file of X-Y-format

    :type filename: string
    :param filename: name of the file to be saved

    :type xx: nparray
    :param xx: the x values to be stored

    :type yy: nparray
    :param yy: the y values to be stored
    """
    datastring = ""
    for (index, element) in enumerate(xx):
        if index != 0:
            datastring += "\n"
        datastring += str(element)
        if str(yy[index]) != "":
            datastring += " "
        datastring += str(yy[index])

    with open(filename, "w") as file:
        file.write(datastring)

def save_nxyformat(filename, xx, yy):
    """
    can be used to save an array of format NxM into a file of N-X-Y-format

    :type filename: string
    :param filename: name of the file to be saved

    :type xx: nparray
    :param xx: the x values to be stored

    :type yy: nparray
    :param yy: multiple columns of y values to be stored
    """
    datastring = ""
    for (index, element) in enumerate(xx):
        if index != 0:
            datastring += "\n"
        datastring += str(element)
        if str(yy[index]) != "":
            datastring += " "
        datastring += " ".join(map(str, yy[index]))

    with open(filename, "w") as file:
        file.write(datastring)
