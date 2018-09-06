#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:05:31 2018

@author: Anton
"""

import eigensolver as es

inputpath = input("Please enter path of input file:\n")
outputpath = input("Where do you want to save the results?\n")
es.calculate_and_save_results(inputpath, outputpath, save=True, plot=True)
