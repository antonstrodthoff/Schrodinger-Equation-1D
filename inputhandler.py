#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:11:17 2018

@author: tillsmac
"""
def input_solve_settings():
    """
    Takes input of the user regarding the solve settings

    :rtype: (string, string)
    :returns: the input- and ouputpath of the data
    """
    inputpath = "schrodinger.inp"
    outputpath = "."

    if input("Do you want to change the default settings? [y/n]\n").lower() == "y":
        inputpath = input("Please enter name of input file:\n")
        outputpath = input("Where do you want to save the results?\n")

    return (inputpath, outputpath)

def input_plot_settings():
    """
    Takes input of the user regarding the plot settings

    :rtype: (string, float, boolean, [float])
    :returns: the settings specified by the user
    """
    inputpath = "."
    scalingfactor = 0
    changerange = False
    axisrange = []

    if input("Do you want to change the default settings? [y/n]\n").lower() == "y":
        inputpath = input("Please enter directory of the input .dat files:\n")
        inputpath = inputpath.replace("//", "/")
        scalingfactor = float(input("Enter scaling factor for eigenstates (0 = autoscale):\n"))
        if input("Do you want to change the axis range? [y/n]\n").lower() == "y":
            changerange = True
            axisrange = input("Enter xmin, xmax, ymin, ymax (seperated by \",\"):\n").split(",")
            axisrange = list(map(float, axisrange))

    return (inputpath, scalingfactor, changerange, axisrange)
