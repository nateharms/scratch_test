#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 3,
    'O': 2,
}

bonds = {
    'C=O': 1,
    'C-O': 1,
    'O-H': 1,
    'C-C': 2,
    'C-H': 5,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AKXKFZDCRYJKTF-UHFFFAOYSA.log'),
}

geometry = GaussianLog('AKXKFZDCRYJKTF-UHFFFAOYSA.log')

frequencies = GaussianLog('AKXKFZDCRYJKTF-UHFFFAOYSA.log')

rotors = []
