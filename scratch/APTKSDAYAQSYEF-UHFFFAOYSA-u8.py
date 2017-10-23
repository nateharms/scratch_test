#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 13,
    'C': 8,
}

bonds = {
    'C-C': 5,
    'C=C': 2,
    'C-H': 13,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('APTKSDAYAQSYEF-UHFFFAOYSA-u8.log'),
}

geometry = GaussianLog('APTKSDAYAQSYEF-UHFFFAOYSA-u8.log')

frequencies = GaussianLog('APTKSDAYAQSYEF-UHFFFAOYSA-u8.log')

rotors = []
