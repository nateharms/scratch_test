#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 2,
    'C': 1,
    'O': 4,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[OH]+[O]OC=O_O=COO+[O].log'),
}

geometry = GaussianLog('[OH]+[O]OC=O_O=COO+[O].log')

frequencies = GaussianLog('[OH]+[O]OC=O_O=COO+[O].log')

rotors = []
