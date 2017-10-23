#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 4,
    'C': 2,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-H': 4,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ALPNRGFNSBABCF-UHFFFAOYSA-u1,2.log'),
}

geometry = GaussianLog('ALPNRGFNSBABCF-UHFFFAOYSA-u1,2.log')

frequencies = GaussianLog('ALPNRGFNSBABCF-UHFFFAOYSA-u1,2.log')

rotors = []
