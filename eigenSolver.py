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

if interType == "polynomial":
    yPotInter = KroghInterpolator(xPot, yPot)
else:
    yPotInter = interp1d(xPot, yPot, kind=interType)

rd.saveXYFormat("potential.dat", xAxis, yPotInter(xAxis))

(eigenVals, eigenVecs) = eigh_tridiagonal(yPotInter(xAxis)+a, np.full(n-1,-1/2*a), select="i", select_range=(fval,lval))

normEigenVecs = np.array([normalize(eigenVec) for eigenVec in eigenVecs.T])

rd.saveNXYFormat("wavefuncs.dat", xAxis, normEigenVecs.T)
rd.saveXYFormat("energies.dat", eigenVals, ["" for _ in eigenVals])

plt.plot(xAxis, eigenVecs[:, 2])
plt.plot(xAxis, yPotInter(xAxis)/100)
plt.show()