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

if interType == "polynomial":
    yPotInter = KroghInterpolator(xPot, yPot)
else:
    yPotInter = interp1d(xPot, yPot, kind=interType)
    
e = eigh_tridiagonal(yPotInter(xAxis)+a, np.full(n-1,-1/2*a), select="i", select_range=(fval,lval))
    
plt.plot(xAxis, yPotInter(xAxis))
plt.show()