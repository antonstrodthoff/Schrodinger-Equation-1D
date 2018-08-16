#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:05:31 2018

@author: Anton
"""

import eigensolver as es

SOLVER = es.Eigensolver()

SOLVER.interpolate()
SOLVER.calculate_results()
SOLVER.save_results()
SOLVER.plot(5)
