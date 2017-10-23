#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 6,
    'O': 2,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O].log'),
}

geometry = GaussianLog('[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O].log')

frequencies = GaussianLog('[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O].log')

rotors = []
