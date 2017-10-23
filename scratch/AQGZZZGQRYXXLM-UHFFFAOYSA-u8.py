#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 19,
    'C': 10,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 9,
    'C-H': 19,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AQGZZZGQRYXXLM-UHFFFAOYSA-u8.log'),
}

geometry = GaussianLog('AQGZZZGQRYXXLM-UHFFFAOYSA-u8.log')

frequencies = GaussianLog('AQGZZZGQRYXXLM-UHFFFAOYSA-u8.log')

rotors = []
