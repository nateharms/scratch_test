#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('TUJKJAMUKRIRHC-UHFFFAOYSA-u1', '/gss_gpfs_scratch/harms.n/QMscratch/TUJKJAMUKRIRHC-UHFFFAOYSA-u1.py')
species('RIIXPRSOZPRLBL-UHFFFAOYSA-u3', '/gss_gpfs_scratch/harms.n/QMscratch/RIIXPRSOZPRLBL-UHFFFAOYSA-u3.py')
species('SCKXCAADGDQQCS-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/SCKXCAADGDQQCS-UHFFFAOYSA.py')
species('QVGXLLKOCUKJST-UHFFFAOYSA-u1,1', '/gss_gpfs_scratch/harms.n/QMscratch/QVGXLLKOCUKJST-UHFFFAOYSA-u1,1.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[OH]+[O]OC=O_O=COO+[O].py')

reaction(
    label = '[OH]+[O]OC=O_O=COO+[O]',
    reactants = ['TUJKJAMUKRIRHC-UHFFFAOYSA-u1', 'RIIXPRSOZPRLBL-UHFFFAOYSA-u3'],
    products = ['SCKXCAADGDQQCS-UHFFFAOYSA', 'QVGXLLKOCUKJST-UHFFFAOYSA-u1,1'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[OH]+[O]OC=O_O=COO+[O]')
