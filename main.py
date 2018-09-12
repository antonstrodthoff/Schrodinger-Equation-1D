#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:05:31 2018

@author: Anton
"""

import eigensolver as es
import inputhandler as ih

(INPUTPATH, OUTPUTPATH) = ih.input_solve_settings()

es.calculate_and_save_results(INPUTPATH, OUTPUTPATH)
