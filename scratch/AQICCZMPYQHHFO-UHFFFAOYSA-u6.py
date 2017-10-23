#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 11,
    'C': 5,
    'O': 2,
}

bonds = {
    'C-O': 1,
    'C-C': 4,
    'O-O': 1,
    'C-H': 11,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AQICCZMPYQHHFO-UHFFFAOYSA-u6.log'),
}

geometry = GaussianLog('AQICCZMPYQHHFO-UHFFFAOYSA-u6.log')

frequencies = GaussianLog('AQICCZMPYQHHFO-UHFFFAOYSA-u6.log')

rotors = []
