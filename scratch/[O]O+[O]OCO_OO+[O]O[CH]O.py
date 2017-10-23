#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 4,
    'C': 1,
    'O': 5,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[O]O+[O]OCO_OO+[O]O[CH]O.log'),
}

geometry = GaussianLog('[O]O+[O]OCO_OO+[O]O[CH]O.log')

frequencies = GaussianLog('[O]O+[O]OCO_OO+[O]O[CH]O.log')

rotors = []
