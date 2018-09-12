#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:54:52 2018

@author: Anton
"""

import inputhandler as ih
import grapher as gr

(INPUTPATH, SCALINGFACTOR, CHANGERANGE, AXISRANGE) = ih.input_plot_settings()

gr.plot(INPUTPATH, SCALINGFACTOR, CHANGERANGE, AXISRANGE)
