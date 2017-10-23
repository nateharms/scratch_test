#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 14,
    'C': 7,
    'O': 1,
}

bonds = {
    'C=O': 1,
    'C-C': 6,
    'C-H': 14,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AZASWMGVGQEVCS-UHFFFAOYSA.log'),
}

geometry = GaussianLog('AZASWMGVGQEVCS-UHFFFAOYSA.log')

frequencies = GaussianLog('AZASWMGVGQEVCS-UHFFFAOYSA.log')

rotors = []
