#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:27:16 2018

@author: Anton
"""

import numpy as np

class Datareader:
    """
    Docstring
    """

    specifications = []

    def __init__(self):
        """
        Docstring
        """
        with open("schrodinger.inp", "r") as datafile:
            data = datafile.read()

        data = data.replace("\n", " ")
        data = data.split(" ")

        for string in data:
            if string == "linear" or string == "polynomial":
                self.specifications.append(string)
            elif string == "cspline":
                self.specifications.append("cubic")
            try:
                self.specifications.append(float(string))
            except ValueError:
                continue

    def particle_mass(self):
        """
        Docstring
        """
        return self.specifications[0]

    def x_minimum(self):
        """
        Docstring
        """
        return self.specifications[1]

    def x_maximum(self):
        """
        Docstring
        """
        return self.specifications[2]

    def n_point(self):
        """
        Docstring
        """
        return int(self.specifications[3])

    def first_eigenvalue(self):
        """
        Docstring
        """
        return int(self.specifications[4])

    def last_eigenvalue(self):
        """
        Docstring
        """
        return int(self.specifications[5])

    def interpolation_type(self):
        """
        Docstring
        """
        return self.specifications[6]

    def interpolation_points(self):
        """
        Docstring
        """
        return self.specifications[7]

    def x_potential(self):
        """
        Docstring
        """
        x_pot = np.array(self.specifications[8:len(self.specifications):2])
        last_x = -100
        for (index, xx) in enumerate(x_pot):
            if xx == last_x:
                x_pot[index] += 0.0000001
            last_x = xx
        return x_pot

    def y_potential(self):
        """
        Docstring
        """
        return np.array(self.specifications[9:len(self.specifications):2])

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
