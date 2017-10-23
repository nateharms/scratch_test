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
    'M062X/MG3S': GaussianLog('AGFMQEQTOYDNLY-UHFFFAOYSA-u2.log'),
}

geometry = GaussianLog('AGFMQEQTOYDNLY-UHFFFAOYSA-u2.log')

frequencies = GaussianLog('AGFMQEQTOYDNLY-UHFFFAOYSA-u2.log')

rotors = []
