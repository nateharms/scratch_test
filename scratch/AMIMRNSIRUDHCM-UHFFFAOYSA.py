#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 4,
    'O': 1,
}

bonds = {
    'C=O': 1,
    'C-C': 3,
    'C-H': 8,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AMIMRNSIRUDHCM-UHFFFAOYSA.log'),
}

geometry = GaussianLog('AMIMRNSIRUDHCM-UHFFFAOYSA.log')

frequencies = GaussianLog('AMIMRNSIRUDHCM-UHFFFAOYSA.log')

rotors = []
