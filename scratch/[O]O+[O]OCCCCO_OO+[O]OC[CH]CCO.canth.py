#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('OISZWBALCPXEMC-UHFFFAOYSA-u6', '/gss_gpfs_scratch/harms.n/QMscratch/OISZWBALCPXEMC-UHFFFAOYSA-u6.py')
species('OUUQCZGPVNCOIJ-UHFFFAOYSA-u2', '/gss_gpfs_scratch/harms.n/QMscratch/OUUQCZGPVNCOIJ-UHFFFAOYSA-u2.py')
species('MHAJPDPJQMAIIY-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/MHAJPDPJQMAIIY-UHFFFAOYSA.py')
species('ODUCIJQWFNXZIJ-UHFFFAOYSA-u2,6', '/gss_gpfs_scratch/harms.n/QMscratch/ODUCIJQWFNXZIJ-UHFFFAOYSA-u2,6.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO.py')

reaction(
    label = '[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO',
    reactants = ['OISZWBALCPXEMC-UHFFFAOYSA-u6', 'OUUQCZGPVNCOIJ-UHFFFAOYSA-u2'],
    products = ['MHAJPDPJQMAIIY-UHFFFAOYSA', 'ODUCIJQWFNXZIJ-UHFFFAOYSA-u2,6'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[O]O+[O]OCCCCO_OO+[O]OC[CH]CCO')
