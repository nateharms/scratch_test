#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 1,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('C+[H]_[CH3]+[H][H].log'),
}

geometry = GaussianLog('C+[H]_[CH3]+[H][H].log')

frequencies = GaussianLog('C+[H]_[CH3]+[H][H].log')

rotors = []
