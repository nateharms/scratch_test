#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 4,
}

bonds = {
    'C-C': 1,
    'C=C': 2,
    'C-H': 5,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AHZKOHHBQMSKLP-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AHZKOHHBQMSKLP-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AHZKOHHBQMSKLP-UHFFFAOYSA-u1.log')

rotors = []
