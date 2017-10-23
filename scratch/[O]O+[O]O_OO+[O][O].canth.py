#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('OUUQCZGPVNCOIJ-UHFFFAOYSA-u2', '/gss_gpfs_scratch/harms.n/QMscratch/OUUQCZGPVNCOIJ-UHFFFAOYSA-u2.py')
species('MHAJPDPJQMAIIY-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/MHAJPDPJQMAIIY-UHFFFAOYSA.py')
species('MYMOFIZGZYHOMD-UHFFFAOYSA-u1,2', '/gss_gpfs_scratch/harms.n/QMscratch/MYMOFIZGZYHOMD-UHFFFAOYSA-u1,2.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[O]O+[O]O_OO+[O][O].py')

reaction(
    label = '[O]O+[O]O_OO+[O][O]',
    reactants = ['OUUQCZGPVNCOIJ-UHFFFAOYSA-u2', 'OUUQCZGPVNCOIJ-UHFFFAOYSA-u2'],
    products = ['MHAJPDPJQMAIIY-UHFFFAOYSA', 'MYMOFIZGZYHOMD-UHFFFAOYSA-u1,2'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[O]O+[O]O_OO+[O][O]')
