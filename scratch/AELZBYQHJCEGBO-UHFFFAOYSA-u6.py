#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 11,
    'C': 5,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'C-C': 4,
    'C-H': 11,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AELZBYQHJCEGBO-UHFFFAOYSA-u6.log'),
}

geometry = GaussianLog('AELZBYQHJCEGBO-UHFFFAOYSA-u6.log')

frequencies = GaussianLog('AELZBYQHJCEGBO-UHFFFAOYSA-u6.log')

rotors = []
