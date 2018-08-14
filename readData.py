#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:27:16 2018

@author: Anton
"""

import numpy as np

with open("schrodinger.inp", "r") as dataFile:
    data = dataFile.read()
    
data = data.replace("\n", " ")
data = data.split(" ")

specifications = []

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

def xMin():
    return specifications[1]

def xMax():
    return specifications[2]

def nPoint():
    return specifications[3]

def firstEigenVal():
    return specifications[4]

def lastEigenVal():
    return specifications[5]

def interpolationType():
    return specifications[6]

def interPoints():
    return specifications[7]

def xPot():
    return np.array(specifications[8:len(specifications):2])
    
def yPot():
    return np.array(specifications[9:len(specifications):2])
