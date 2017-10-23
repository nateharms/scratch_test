#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 17,
    'C': 8,
}

bonds = {
    'C-C': 7,
    'C-H': 17,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AUNGTSCVKGQIAH-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AUNGTSCVKGQIAH-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AUNGTSCVKGQIAH-UHFFFAOYSA-u1.log')

rotors = []
