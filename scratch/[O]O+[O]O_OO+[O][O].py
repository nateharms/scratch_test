#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 2,
    'O': 4,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[O]O+[O]O_OO+[O][O].log'),
}

geometry = GaussianLog('[O]O+[O]O_OO+[O][O].log')

frequencies = GaussianLog('[O]O+[O]O_OO+[O][O].log')

rotors = []
