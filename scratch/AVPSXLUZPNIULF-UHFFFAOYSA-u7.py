#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 15,
    'C': 8,
}

bonds = {
    'C=C': 1,
    'C-C': 6,
    'C-H': 15,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M062X/MG3S': GaussianLog('AVPSXLUZPNIULF-UHFFFAOYSA-u7.log'),
}

geometry = GaussianLog('AVPSXLUZPNIULF-UHFFFAOYSA-u7.log')

frequencies = GaussianLog('AVPSXLUZPNIULF-UHFFFAOYSA-u7.log')

rotors = []
