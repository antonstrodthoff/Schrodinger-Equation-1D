#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:41:54 2018

@author: Anton
"""

import readData as rd
import numpy as np
from scipy.interpolate import interp1d, KroghInterpolator
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

m = rd.mass()
xMin = rd.xMinimum()
xMax = rd.xMaximum()
n = rd.nPoint()
fval = rd.firstEigenValue()
lval = rd.lastEigenValue()
interType = rd.interpolationType()
interPoints = rd.interpolationPoints()
xPot = rd.xPotential()
yPot = rd.yPotential()
delta = (xMax-xMin)/n
a = 1/(m*delta**2)
xAxis = np.linspace(xMin, xMax, n)
yPotInter = []
energies = np.array([])
normEigenVecs = np.array([])
expectedX = np.array([])
uncertainties = np.array([])

def norm(vector):
    s = 0
    for element in vector:
        s += element**2
    return (s*delta)**(1/2)

def normalize(vector):
    factor = norm(vector)
    for (index, element) in enumerate(vector):
        vector[index] /= factor
    return vector

def expX(vector):
    s = 0
    for (index, element) in enumerate(vector):
        s += xAxis[index]*element**2
    return delta*s

def expXSqrd(vector):
    s = 0
    for (index, element) in enumerate(vector):
        s += xAxis[index]**2*element**2
    return delta*s

def uncertainty(vector):
    return (expXSqrd(vector)-expX(vector)**2)**(1/2)

def interpolate():
    global yPotInter
    if interType == "polynomial":
        yPotInter = KroghInterpolator(xPot, yPot)
    else:
        yPotInter = interp1d(xPot, yPot, kind=interType)
    
def calculateResults():
    global expectedX, uncertainties, energies, normEigenVecs
    (energies, eigenVecs) = eigh_tridiagonal(yPotInter(xAxis)+a, np.full(n-1,-1/2*a), select="i", select_range=(fval-1,lval-1))
    normEigenVecs = np.array([normalize(eigenVec) for eigenVec in eigenVecs.T])
    expectedX = np.array([expX(eigenVec) for eigenVec in normEigenVecs])
    uncertainties = np.array([uncertainty(eigenVec) for eigenVec in normEigenVecs])

def saveResults():
    rd.saveXYFormat("potential.dat", xAxis, yPotInter(xAxis))
    rd.saveNXYFormat("wavefuncs.dat", xAxis, normEigenVecs.T)
    rd.saveXYFormat("energies.dat", energies, ["" for _ in energies])
    rd.saveXYFormat("expvalues.dat", expectedX, uncertainties)

interpolate()
calculateResults()
saveResults()

plt.plot(xAxis, normEigenVecs[3])
plt.plot(xAxis, yPotInter(xAxis)/10)
plt.show()