#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:27:16 2018

@author: Anton
"""

import numpy as np

SPECIFICATIONS = []

def load_data(file):
    """
    Docstring
    """
    with open(file, "r") as datafile:
        data = datafile.read()

    data = data.replace("\n", " ")
    data = data.split(" ")

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
    Docstring
    """
    return SPECIFICATIONS[0]

def x_minimum():
    """
    Docstring
    """
    return SPECIFICATIONS[1]

def x_maximum():
    """
    Docstring
    """
    return SPECIFICATIONS[2]

def n_point():
    """
    Docstring
    """
    return int(SPECIFICATIONS[3])

def first_eigenvalue():
    """
    Docstring
    """
    return int(SPECIFICATIONS[4])

def last_eigenvalue():
    """
    Docstring
    """
    return int(SPECIFICATIONS[5])

def interpolation_type():
    """
    Docstring
    """
    return SPECIFICATIONS[6]

def interpolation_points():
    """
    Docstring
    """
    return SPECIFICATIONS[7]

def x_potential():
    """
    Docstring
    """
    x_pot = np.array(SPECIFICATIONS[8:len(SPECIFICATIONS):2])
    last_x = -100
    for (index, xx) in enumerate(x_pot):
        if xx == last_x:
            x_pot[index] += 0.0000001
        last_x = xx
    return x_pot

def y_potential():
    """
    Docstring
    """
    return np.array(SPECIFICATIONS[9:len(SPECIFICATIONS):2])

def read_xyformat(filename):
    """
    Docstring
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
    Docstring
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
    Docstring
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
