#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('C', '../../../../Species/C/m062x/C.py')
species('[H]', '../../../../Species/[H]/m062x/[H].py')
species('[H][H]', '../../../../Species/[H][H]/m062x/[H][H].py')
species('[CH3]', '../../../../Species/[CH3]/m062x/[CH3].py')
transitionState('TS', '/scratch/bhoorasingh.p/QMfiles/Reactions/H_Abstraction/C+[H]_[CH3]+[H][H]/m062x/C+[H]_[CH3]+[H][H].py')

reaction(
    label = 'C+[H]_[CH3]+[H][H]',
    reactants = ['C', '[H]'],
    products = ['[H][H]', '[CH3]'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('C+[H]_[CH3]+[H][H]')
