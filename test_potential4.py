#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 12:16:53 2018

@author: Anton
"""

import pytest
import eigensolver as es
import readdata as rd

INPUTPATH = "test_potentials/test_schrodinger4.inp"
OUTPUTPATH = "test_potentials/test_results4"
es.calculate_and_save_results(INPUTPATH, OUTPUTPATH)

def test_results4_potential():
    """
    compares the calculated potential to already verified reference data
    """
    potential = rd.read_xyformat("test_potentials/test_results4/potential.dat")
    potential_reference = rd.read_xyformat("test_potentials/test_results4_reference/potential.dat")

    assert potential == pytest.approx(potential_reference)

def test_results4_wavefuncs():
    """
    compares the calculated eigenstates to already verified reference data
    """
    wavefuncs = rd.read_xyformat("test_potentials/test_results4/wavefuncs.dat")
    wavefuncs_reference = rd.read_xyformat("test_potentials/test_results4_reference/wavefuncs.dat")

    assert wavefuncs == pytest.approx(wavefuncs_reference)

def test_results4_energies():
    """
    compares the calculated eigenvalues to already verified reference data
    """
    energies = rd.read_xyformat("test_potentials/test_results4/energies.dat")
    energies_reference = rd.read_xyformat("test_potentials/test_results4_reference/energies.dat")

    assert energies == pytest.approx(energies_reference)

def test_results4_expvalues():
    """
    compares the calculated expected values to already verified reference data
    """
    expvals = rd.read_xyformat("test_potentials/test_results4/expvalues.dat")
    expvals_reference = rd.read_xyformat("test_potentials/test_results4_reference/expvalues.dat")

    assert expvals == pytest.approx(expvals_reference)
