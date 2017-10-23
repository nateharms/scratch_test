#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 9,
    'C': 5,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 4,
    'C-H': 9,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ADJPNXDTTBCKTM-UHFFFAOYSA-u4.log'),
}

geometry = GaussianLog('ADJPNXDTTBCKTM-UHFFFAOYSA-u4.log')

frequencies = GaussianLog('ADJPNXDTTBCKTM-UHFFFAOYSA-u4.log')

rotors = []
