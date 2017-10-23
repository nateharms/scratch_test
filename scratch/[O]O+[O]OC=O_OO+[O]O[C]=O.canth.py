#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('RIIXPRSOZPRLBL-UHFFFAOYSA-u3', '/gss_gpfs_scratch/harms.n/QMscratch/RIIXPRSOZPRLBL-UHFFFAOYSA-u3.py')
species('OUUQCZGPVNCOIJ-UHFFFAOYSA-u2', '/gss_gpfs_scratch/harms.n/QMscratch/OUUQCZGPVNCOIJ-UHFFFAOYSA-u2.py')
species('MHAJPDPJQMAIIY-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/MHAJPDPJQMAIIY-UHFFFAOYSA.py')
species('ITVFZPAJODSVMF-UHFFFAOYSA-u1,3', '/gss_gpfs_scratch/harms.n/QMscratch/ITVFZPAJODSVMF-UHFFFAOYSA-u1,3.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[O]O+[O]OC=O_OO+[O]O[C]=O.py')

reaction(
    label = '[O]O+[O]OC=O_OO+[O]O[C]=O',
    reactants = ['RIIXPRSOZPRLBL-UHFFFAOYSA-u3', 'OUUQCZGPVNCOIJ-UHFFFAOYSA-u2'],
    products = ['MHAJPDPJQMAIIY-UHFFFAOYSA', 'ITVFZPAJODSVMF-UHFFFAOYSA-u1,3'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[O]O+[O]OC=O_OO+[O]O[C]=O')
