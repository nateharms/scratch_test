#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C=C': 1,
    'C-C': 2,
    'C-H': 6,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ARGCQEVBJHPOGB-UHFFFAOYSA.log'),
}

geometry = GaussianLog('ARGCQEVBJHPOGB-UHFFFAOYSA.log')

frequencies = GaussianLog('ARGCQEVBJHPOGB-UHFFFAOYSA.log')

rotors = []
