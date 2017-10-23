#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 11,
    'C': 6,
    'O': 1,
}

bonds = {
    'C=O': 1,
    'C-C': 5,
    'C-H': 11,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AZYNPBUFXQHLBD-UHFFFAOYSA-u3.log'),
}

geometry = GaussianLog('AZYNPBUFXQHLBD-UHFFFAOYSA-u3.log')

frequencies = GaussianLog('AZYNPBUFXQHLBD-UHFFFAOYSA-u3.log')

rotors = []
