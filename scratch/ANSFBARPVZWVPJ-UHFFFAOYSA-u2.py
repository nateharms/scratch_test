#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 5,
    'O': 1,
}

bonds = {
    'C=O': 1,
    'C=C': 1,
    'C-C': 3,
    'C-H': 7,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ANSFBARPVZWVPJ-UHFFFAOYSA-u2.log'),
}

geometry = GaussianLog('ANSFBARPVZWVPJ-UHFFFAOYSA-u2.log')

frequencies = GaussianLog('ANSFBARPVZWVPJ-UHFFFAOYSA-u2.log')

rotors = []
