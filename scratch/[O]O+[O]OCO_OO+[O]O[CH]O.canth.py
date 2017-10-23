#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('OLHGCLQZCFQBGO-UHFFFAOYSA-u3', '/gss_gpfs_scratch/harms.n/QMscratch/OLHGCLQZCFQBGO-UHFFFAOYSA-u3.py')
species('OUUQCZGPVNCOIJ-UHFFFAOYSA-u2', '/gss_gpfs_scratch/harms.n/QMscratch/OUUQCZGPVNCOIJ-UHFFFAOYSA-u2.py')
species('MHAJPDPJQMAIIY-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/MHAJPDPJQMAIIY-UHFFFAOYSA.py')
species('MMYFBIMHRWJTSD-UHFFFAOYSA-u1,3', '/gss_gpfs_scratch/harms.n/QMscratch/MMYFBIMHRWJTSD-UHFFFAOYSA-u1,3.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[O]O+[O]OCO_OO+[O]O[CH]O.py')

reaction(
    label = '[O]O+[O]OCO_OO+[O]O[CH]O',
    reactants = ['OLHGCLQZCFQBGO-UHFFFAOYSA-u3', 'OUUQCZGPVNCOIJ-UHFFFAOYSA-u2'],
    products = ['MHAJPDPJQMAIIY-UHFFFAOYSA', 'MMYFBIMHRWJTSD-UHFFFAOYSA-u1,3'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[O]O+[O]OCO_OO+[O]O[CH]O')
