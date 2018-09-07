#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 12:16:53 2018

@author: Anton
"""

import pytest
import eigensolver as es
import readdata as rd

INPUTPATH = "test_potentials/test_schrodinger1.inp"
OUTPUTPATH = "test_potentials/test_results1"
es.calculate_and_save_results(INPUTPATH, OUTPUTPATH)

def test_results1_potential():
    """
    compares the calculated potential to already verified reference data
    """
    potential = rd.read_xyformat("test_potentials/test_results1/potential.dat")
    potential_reference = rd.read_xyformat("test_potentials/test_results1_reference/potential.dat")

    assert potential == pytest.approx(potential_reference)

def test_results1_wavefuncs():
    """
    compares the calculated eigenstates to already verified reference data
    """
    wavefuncs = rd.read_xyformat("test_potentials/test_results1/wavefuncs.dat")
    wavefuncs_reference = rd.read_xyformat("test_potentials/test_results1_reference/wavefuncs.dat")

    assert wavefuncs == pytest.approx(wavefuncs_reference)

def test_results1_energies():
    """
    compares the calculated eigenvalues to already verified reference data
    """
    energies = rd.read_xyformat("test_potentials/test_results1/energies.dat")
    energies_reference = rd.read_xyformat("test_potentials/test_results1_reference/energies.dat")

    assert energies == pytest.approx(energies_reference)

def test_results1_expvalues():
    """
    compares the calculated expected values to already verified reference data
    """
    expvals = rd.read_xyformat("test_potentials/test_results1/expvalues.dat")
    expvals_reference = rd.read_xyformat("test_potentials/test_results1_reference/expvalues.dat")

    assert expvals == pytest.approx(expvals_reference)
