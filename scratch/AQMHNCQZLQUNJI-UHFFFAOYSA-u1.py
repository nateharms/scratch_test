#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 15,
    'C': 7,
}

bonds = {
    'C-C': 6,
    'C-H': 15,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AQMHNCQZLQUNJI-UHFFFAOYSA-u1.log'),
}

geometry = GaussianLog('AQMHNCQZLQUNJI-UHFFFAOYSA-u1.log')

frequencies = GaussianLog('AQMHNCQZLQUNJI-UHFFFAOYSA-u1.log')

rotors = []
