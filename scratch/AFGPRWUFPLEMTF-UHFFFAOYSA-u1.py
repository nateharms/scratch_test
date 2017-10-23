#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 2,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-H': 5,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AFGPRWUFPLEMTF-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AFGPRWUFPLEMTF-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AFGPRWUFPLEMTF-UHFFFAOYSA-u1.log')

rotors = []
