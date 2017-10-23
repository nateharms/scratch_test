#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 3,
}

bonds = {
    'C-C': 2,
    'C-H': 8,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('ATUOYWHBWRKTHZ-UHFFFAOYSA.log'),
}

geometry = GaussianLog('ATUOYWHBWRKTHZ-UHFFFAOYSA.log')

frequencies = GaussianLog('ATUOYWHBWRKTHZ-UHFFFAOYSA.log')

rotors = []
