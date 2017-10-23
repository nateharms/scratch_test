#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 3,
    'C': 3,
    'O': 3,
}

bonds = {
    'C-O': 2,
    'C=O': 2,
    'C-C': 1,
    'C-H': 3,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AALLQROOJJSXFA-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AALLQROOJJSXFA-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AALLQROOJJSXFA-UHFFFAOYSA-u1.log')

rotors = []
