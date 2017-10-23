#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 8,
    'O': 1,
}

bonds = {
    'C=O': 1,
    'C=C': 3,
    'C-C': 5,
    'C-H': 7,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AESCIILLFQQVSC-UHFFFAOYSA-u2.log'),
}

geometry = GaussianLog('AESCIILLFQQVSC-UHFFFAOYSA-u2.log')

frequencies = GaussianLog('AESCIILLFQQVSC-UHFFFAOYSA-u2.log')

rotors = []
