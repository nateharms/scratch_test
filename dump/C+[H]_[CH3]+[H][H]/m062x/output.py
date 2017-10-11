# Coordinates for C (angstroms):
#   C    0.0000    0.0000    0.0000
#   H    0.9062   -0.5959    0.0706
#   H    0.2165    0.9274   -0.5236
#   H   -0.3651    0.2246    0.9987
#   H   -0.7577   -0.5559   -0.5460
conformer(
    label = 'C',
    E0 = (-76.3171, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(16.0313, 'amu')),
        NonlinearRotor(
            inertia = ([3.17388, 3.17478, 3.17494], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([1315.44, 1317.28, 1321.83, 1535.77, 1540.66, 2996.67, 3107.35, 3108.72, 3111], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Coordinates for [H] (angstroms):
#   H    0.0000    0.0000    0.0000
conformer(
    label = '[H]',
    E0 = (211.794, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(1.00783, 'amu')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Coordinates for [H][H] (angstroms):
#   H    0.0000    0.0000    0.0000
#   H   -0.7383    0.0000    0.0000
conformer(
    label = '[H][H]',
    E0 = (-2.99057, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(2.01565, 'amu')),
        LinearRotor(inertia=(0.274682, 'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([4390.65], 'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Coordinates for [CH3] (angstroms):
#   C    0.0000    0.0000    0.0000
#   H    1.0709   -0.1101   -0.0012
#   H   -0.6304   -0.8728    0.0062
#   H   -0.4404    0.9823   -0.0073
conformer(
    label = '[CH3]',
    E0 = (141.075, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(15.0235, 'amu')),
        NonlinearRotor(
            inertia = ([1.75167, 1.7526, 3.50427], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([435.712, 1387.77, 1390.09, 3083.04, 3251.22, 3266.91], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Coordinates for TS (angstroms):
#   H    0.0000    0.0000    0.0000
#   C   -2.2856    0.0788   -0.0391
#   H   -0.8933    0.0302   -0.0150
#   H   -2.5546   -0.8195   -0.5807
#   H   -2.5518    0.0766    1.0104
#   H   -2.4910    1.0052   -0.5606
conformer(
    label = 'TS',
    E0 = (193.17, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(17.0391, 'amu')),
        NonlinearRotor(
            inertia = ([3.36042, 8.57901, 8.57932], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([470.924, 475.92, 1055.89, 1064.23, 1065.06, 1410.18, 1411.72, 1685.32, 3032.88, 3173.44, 3181.26], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    frequency = (-1573.77, 'cm^-1'),
)

#   ======= =========== =========== =========== ===============
#   Temp.   k (TST)     Tunneling   k (TST+T)   Units
#   ======= =========== =========== =========== ===============
#     300 K   1.320e+03     24.5329   3.238e+04 cm^3/(mol*s)
#     400 K   4.609e+05     4.84458   2.233e+06 cm^3/(mol*s)
#     500 K   1.678e+07     2.61795   4.394e+07 cm^3/(mol*s)
#     600 K   1.966e+08     1.93082   3.797e+08 cm^3/(mol*s)
#     800 K   4.829e+09      1.4494   7.000e+09 cm^3/(mol*s)
#    1000 K   3.673e+10     1.27364   4.679e+10 cm^3/(mol*s)
#    1500 K   6.871e+11     1.12078   7.701e+11 cm^3/(mol*s)
#    2000 K   3.500e+12     1.07048   3.746e+12 cm^3/(mol*s)
#   ======= =========== =========== =========== ===============
kinetics(
    label = 'C+[H]_[CH3]+[H][H]',
    kinetics = Arrhenius(
        A = (119.435, 'cm^3/(mol*s)'),
        n = 3.47837,
        Ea = (36.2331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.04619, dn = +|- 0.0939659, dEa = +|- 0.516907 kJ/mol',
    ),
)

