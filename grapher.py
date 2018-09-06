#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:20:55 2018

@author: tillsmac
"""

import matplotlib.pyplot as plt
import readdata as rd

reader = rd.Datareader()

wavefuncs = rd.read_xyformat("wavefuncs.dat")
potential = rd.read_xyformat("potential.dat")
energies = rd.read_xyformat("energies.dat")[0]

scalingfactor = float(input("Set scaling factor: "))

f, (ax1, ax2) = plt.subplots(1, 2)

for ii in range(int(reader.last_eigenvalue() + 1 - reader.first_eigenvalue())):
    ax1.plot(wavefuncs[0], [element*scalingfactor + energies[ii] for element in wavefuncs[ii+1]])
    
ax1.plot(potential[0], potential[1])
ax1.set_ylim([min(energies)-abs(min(energies))*0.2, max(energies)+abs(max(energies))*0.2])

plt.show()
