#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 3,
    'O': 2,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('OO+[H]_[H][H]+[O]O.log'),
}

geometry = GaussianLog('OO+[H]_[H][H]+[O]O.log')

frequencies = GaussianLog('OO+[H]_[H][H]+[O]O.log')

rotors = []
