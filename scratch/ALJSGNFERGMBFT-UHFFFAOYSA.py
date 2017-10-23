#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 16,
    'C': 7,
    'O': 2,
}

bonds = {
    'C-O': 1,
    'O-O': 1,
    'O-H': 1,
    'C-C': 6,
    'C-H': 15,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ALJSGNFERGMBFT-UHFFFAOYSA.log'),
}

geometry = GaussianLog('ALJSGNFERGMBFT-UHFFFAOYSA.log')

frequencies = GaussianLog('ALJSGNFERGMBFT-UHFFFAOYSA.log')

rotors = []
