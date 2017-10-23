#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 17,
    'C': 8,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 6,
    'C-H': 17,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AJHJGTHBZDDKLS-UHFFFAOYSA-u3.log'),
}

geometry = GaussianLog('AJHJGTHBZDDKLS-UHFFFAOYSA-u3.log')

frequencies = GaussianLog('AJHJGTHBZDDKLS-UHFFFAOYSA-u3.log')

rotors = []
