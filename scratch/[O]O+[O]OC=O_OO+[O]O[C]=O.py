#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 2,
    'C': 1,
    'O': 5,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[O]O+[O]OC=O_OO+[O]O[C]=O.log'),
}

geometry = GaussianLog('[O]O+[O]OC=O_OO+[O]O[C]=O.log')

frequencies = GaussianLog('[O]O+[O]OC=O_OO+[O]O[C]=O.log')

rotors = []
