#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:05:31 2018

@author: Anton
"""

import eigensolver as es
import grapher as gr
import inputhandler as ih

(INPUTPATH, OUTPUTPATH, SCALINGFACTOR, CHANGERANGE, AXISRANGE) = ih.input_settings()

es.calculate_and_save_results(INPUTPATH, OUTPUTPATH)
gr.plot(SCALINGFACTOR, CHANGERANGE, AXISRANGE)
