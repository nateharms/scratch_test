#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 4,
    'O': 2,
}

bonds = {
    'C-O': 2,
    'C=C': 1,
    'C-C': 1,
    'C=O': 1,
    'C-H': 5,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AYDHKVDAFIGYJU-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AYDHKVDAFIGYJU-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AYDHKVDAFIGYJU-UHFFFAOYSA-u1.log')

rotors = []
