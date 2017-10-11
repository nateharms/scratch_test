#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('OO', '../../../../Species/OO/m062x/OO.py')
species('[H]', '../../../../Species/[H]/m062x/[H].py')
species('[H][H]', '../../../../Species/[H][H]/m062x/[H][H].py')
species('[O]O', '../../../../Species/[O]O/m062x/[O]O.py')
transitionState('TS', '/scratch/bhoorasingh.p/QMfiles/Reactions/H_Abstraction/OO+[H]_[H][H]+[O]O/m062x/OO+[H]_[H][H]+[O]O.py')

reaction(
    label = 'OO+[H]_[H][H]+[O]O',
    reactants = ['OO', '[H]'],
    products = ['[H][H]', '[O]O'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('OO+[H]_[H][H]+[O]O')
