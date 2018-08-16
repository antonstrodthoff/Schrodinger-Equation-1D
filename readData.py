#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:27:16 2018

@author: Anton
"""

import numpy as np

specifications = []

def read():
    global specifications
    with open("schrodinger.inp", "r") as dataFile:
        data = dataFile.read()
    
    data = data.replace("\n", " ")
    data = data.split(" ")

    for string in data:
        if string == "linear" or string == "polynomial":
            specifications.append(string)
        elif string == "cspline":
            specifications.append("cubic")
            
        try:
            specifications.append(float(string))
        except ValueError:
            continue

def mass():
    return specifications[0]

def xMinimum():
    return specifications[1]

def xMaximum():
    return specifications[2]

def nPoint():
    return int(specifications[3])

def firstEigenValue():
    return int(specifications[4])

def lastEigenValue():
    return int(specifications[5])

def interpolationType():
    return specifications[6]

def interpolationPoints():
    return specifications[7]

def xPotential():
    xPot = np.array(specifications[8:len(specifications):2])
    lastx = -100
    for (index, x) in enumerate(xPot):
        if x == lastx:
            xPot[index]+=0.0000001
        lastx = x
    return xPot
    
def yPotential():
    return np.array(specifications[9:len(specifications):2])

"reading XY and NXY formats"
def readXYFormat(fileName):
    dataList = []
    with open(fileName, "r") as dataFile:
        data = dataFile.read()
        data = data.split("\n")
        for element in data:
            dataList.append(element.split(" "))
    return np.array(dataList).T

def saveXYFormat(filename, x, y):
    dataString = ""
    for (index, element) in enumerate(x):
        if index != 0:
            dataString += "\n"
        dataString += str(element)
        if str(y[index]) != "":
            dataString += " "
        dataString += str(y[index])
    
    with open(filename, "w") as file:
        file.write(dataString)
      
def saveNXYFormat(filename, x, y):
    dataString = ""
    for (index, element) in enumerate(x):
        if index != 0:
            dataString += "\n"
        dataString += str(element)
        if str(y[index]) != "":
            dataString += " "
        dataString += " ".join(map(str, y[index]))
    
    with open(filename, "w") as file:
        file.write(dataString)
    
    