#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:20:55 2018

@author: tillsmac
"""

import matplotlib.pyplot as plt
import readdata as rd

def plot(scalingfactor, changerange, axisrange):
    """
    reads the saved files and plots the information
    """
    colorcycle = ["b", "g", "r", "c", "m", "y", "k"]
    activecolor = "b"

    wavefuncs = rd.read_xyformat("wavefuncs.dat")
    potential = rd.read_xyformat("potential.dat")
    energies = rd.read_xyformat("energies.dat")[0]
    expvals = rd.read_xyformat("expvalues.dat")

    _, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    for ii in range(int(rd.last_eigenvalue() + 1 - rd.first_eigenvalue())):
        scaled_wavefunc = [element*scalingfactor + energies[ii] for element in wavefuncs[ii+1]]
        ax1.plot(wavefuncs[0], scaled_wavefunc, color=activecolor)
        ax1.plot(expvals[0][ii], energies[ii], color=activecolor, marker="x")
        ax1.axhline(y=energies[ii], alpha=0.2, color="grey", linewidth=1)
        ax2.plot(expvals[1][ii], energies[ii], color=activecolor, marker="x")
        ax2.axhline(y=energies[ii], alpha=0.2, color="grey", linewidth=1)
        index = (colorcycle.index(activecolor) + 1) % len(colorcycle)
        activecolor = colorcycle[index]

    ax1.plot(potential[0], potential[1])
    ax1.set_ylim([min(energies)-max(abs(energies))*0.1, max(energies)+max(abs(energies))*0.1])
    ax2.set_xlim([0, max(expvals[1])*1.1])
    if changerange:
        ax1.set_xlim([axisrange[0], axisrange[1]])
        ax1.set_ylim([axisrange[2], axisrange[3]])
    ax1.set_title("Potential, Eigenstates, ⟨x⟩")
    ax2.set_title("σ\u2093")
    ax1.set_ylabel("Energy [Hartree]")
    ax1.set_xlabel("x [Bohr]")
    ax2.set_xlabel("x [Bohr]")
    plt.show()
