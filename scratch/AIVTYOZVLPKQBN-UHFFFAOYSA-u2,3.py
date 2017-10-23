#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 5,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 3,
    'C=C': 1,
    'C-H': 6,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AIVTYOZVLPKQBN-UHFFFAOYSA-u2,3.log'),
}

geometry = GaussianLog('AIVTYOZVLPKQBN-UHFFFAOYSA-u2,3.log')

frequencies = GaussianLog('AIVTYOZVLPKQBN-UHFFFAOYSA-u2,3.log')

rotors = []
