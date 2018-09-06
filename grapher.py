#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:20:55 2018

@author: tillsmac
"""

import matplotlib.pyplot as plt
import readdata as rd

def plot():
    colorcycle = ["b", "g", "r", "c", "m", "y", "k"]
    activecolor = "b"
    
    rd.load_data("schrodinger.inp")
    
    wavefuncs = rd.read_xyformat("wavefuncs.dat")
    potential = rd.read_xyformat("potential.dat")
    energies = rd.read_xyformat("energies.dat")[0]
    expected_x = rd.read_xyformat("expvalues.dat")[0]
    uncertainty = rd.read_xyformat("expvalues.dat")[1]
    
    
    scalingfactor = float(input("Set scaling factor: "))
    
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    
    for ii in range(int(rd.last_eigenvalue() + 1 - rd.first_eigenvalue())):
        ax1.plot(wavefuncs[0], [element*scalingfactor + energies[ii] for element in wavefuncs[ii+1]], color=activecolor)
        ax1.plot(expected_x[ii], energies[ii], color=activecolor, marker="x")
        ax1.axhline(y=energies[ii], alpha=0.2, color="grey", linewidth=1)
        ax2.plot(uncertainty[ii], energies[ii], color=activecolor, marker="x")
        ax2.axhline(y=energies[ii], alpha=0.2, color="grey", linewidth=1)
        index = (colorcycle.index(activecolor) + 1) % len(colorcycle)
        activecolor = colorcycle[index]
    
    ax1.plot(potential[0], potential[1])
    ax1.set_ylim([min(energies)-abs(max(energies))*0.1, max(energies)+abs(max(energies))*0.1])
    ax2.set_xlim([0,max(uncertainty)*1.1])
    ax1.set_title("Potential, Eigenstates, ⟨x⟩")
    ax2.set_title("σ\u2093")
    ax1.set_ylabel("Energy [Hartree]")
    ax1.set_xlabel("x [Bohr]")
    ax2.set_xlabel("x [Bohr]")
    plt.show()
