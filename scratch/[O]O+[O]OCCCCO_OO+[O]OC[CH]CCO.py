#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 10,
    'C': 4,
    'O': 5,
}

bonds = {}

linear = False

externalSymmetry = 1

spinMultiplicity = 3

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO.log'),
}

geometry = GaussianLog('[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO.log')

frequencies = GaussianLog('[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO.log')

rotors = []
