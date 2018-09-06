#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:11:17 2018

@author: tillsmac
"""
def input_settings():
    """
    Takes input of the user regarding the settings
    """
    inputpath = "schrodinger.inp"
    outputpath = "."
    scalingfactor = 1
    changerange = False
    axisrange = []

    if input("Do you want to change the default settings? [y/n]\n").lower() == "y":
        inputpath = input("Please enter directory of input file:\n") + "/" + inputpath
        outputpath = input("Where do you want to save the results?\n")
        scalingfactor = float(input("Enter scaling factor for eigenstates:\n"))
        if input("Do you want to change the axis range? [y/n]\n").lower() == "y":
            changerange = True
            axisrange = input("Enter xmin, xmax, ymin, ymax (seperated by \",\"):\n").split(",")
            axisrange = list(map(float, axisrange))

    return (inputpath, outputpath, scalingfactor, changerange, axisrange)
