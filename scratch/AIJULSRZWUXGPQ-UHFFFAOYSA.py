#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 4,
    'C': 3,
    'O': 2,
}

bonds = {
    'C=O': 2,
    'C-C': 2,
    'C-H': 4,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AIJULSRZWUXGPQ-UHFFFAOYSA.log'),
}

geometry = GaussianLog('AIJULSRZWUXGPQ-UHFFFAOYSA.log')

frequencies = GaussianLog('AIJULSRZWUXGPQ-UHFFFAOYSA.log')

rotors = []
