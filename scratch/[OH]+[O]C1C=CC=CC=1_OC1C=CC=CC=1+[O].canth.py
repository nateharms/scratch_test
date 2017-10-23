#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M062X/MG3S"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('TUJKJAMUKRIRHC-UHFFFAOYSA-u1', '/gss_gpfs_scratch/harms.n/QMscratch/TUJKJAMUKRIRHC-UHFFFAOYSA-u1.py')
species('KHUXNRRPPZOJPT-UHFFFAOYSA-u2', '/gss_gpfs_scratch/harms.n/QMscratch/KHUXNRRPPZOJPT-UHFFFAOYSA-u2.py')
species('ISWSIDIOOBJBQZ-UHFFFAOYSA', '/gss_gpfs_scratch/harms.n/QMscratch/ISWSIDIOOBJBQZ-UHFFFAOYSA.py')
species('QVGXLLKOCUKJST-UHFFFAOYSA-u1,1', '/gss_gpfs_scratch/harms.n/QMscratch/QVGXLLKOCUKJST-UHFFFAOYSA-u1,1.py')
transitionState('TS', '/gss_gpfs_scratch/harms.n/QMscratch/[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O].py')

reaction(
    label = '[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O]',
    reactants = ['TUJKJAMUKRIRHC-UHFFFAOYSA-u1', 'KHUXNRRPPZOJPT-UHFFFAOYSA-u2'],
    products = ['ISWSIDIOOBJBQZ-UHFFFAOYSA', 'QVGXLLKOCUKJST-UHFFFAOYSA-u1,1'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('[OH]+[O]C1C=CC=CC=1_OC1C=CC=CC=1+[O]')
