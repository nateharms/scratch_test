#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 13,
    'C': 7,
}

bonds = {
    'C-C': 7,
    'C-H': 13,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AXOLWCUJJCRZPC-UHFFFAOYSA-u2.log'),
}

geometry = GaussianLog('AXOLWCUJJCRZPC-UHFFFAOYSA-u2.log')

frequencies = GaussianLog('AXOLWCUJJCRZPC-UHFFFAOYSA-u2.log')

rotors = []
