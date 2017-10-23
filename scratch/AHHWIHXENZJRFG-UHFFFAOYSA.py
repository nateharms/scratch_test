#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 3,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 2,
    'C-H': 6,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AHHWIHXENZJRFG-UHFFFAOYSA.log'),
}

geometry = GaussianLog('AHHWIHXENZJRFG-UHFFFAOYSA.log')

frequencies = GaussianLog('AHHWIHXENZJRFG-UHFFFAOYSA.log')

rotors = []
