# Coordinates for OO (angstroms):
#   O    0.0000    0.0000    0.0000
#   O    1.1585   -0.8158    0.0951
#   H   -0.6074   -0.5809   -0.4701
#   H    1.7795   -0.3354   -0.4625
conformer(
    label = 'OO',
    E0 = (-134.382, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(34.0055, 'amu')),
        NonlinearRotor(
            inertia = ([1.63801, 18.4022, 19.029], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([378.1, 1029.14, 1344.99, 1458.5, 3786.54, 3787.27], 'cm^-1'),
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

# Coordinates for [O]O (angstroms):
#   O    0.0000    0.0000    0.0000
#   O    1.1585   -0.6019    0.0000
#   H   -0.6688   -0.7053    0.0000
conformer(
    label = '[O]O',
    E0 = (6.19497, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(32.9977, 'amu')),
        NonlinearRotor(
            inertia = ([0.800947, 14.5112, 15.3121], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(frequencies=([1245.9, 1447.19, 3645.15], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Coordinates for TS (angstroms):
#   O    0.0000    0.0000    0.0000
#   O   -1.2530    0.5614   -0.1263
#   H    0.7181    0.8650   -0.0390
#   H   -1.5638    0.6235    0.7853
#   H    1.3203    1.6506   -0.0061
conformer(
    label = 'TS',
    E0 = (106.802, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(35.0133, 'amu')),
        NonlinearRotor(
            inertia = ([5.0648, 20.2194, 23.6683], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([386.884, 462.522, 728.462, 1078.85, 1286.24, 1423.28, 1496.57, 3754.96], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    frequency = (-2094.19, 'cm^-1'),
)

#   ======= =========== =========== =========== ===============
#   Temp.   k (TST)     Tunneling   k (TST+T)   Units
#   ======= =========== =========== =========== ===============
#     300 K   7.173e+07     60.3558   4.329e+09 cm^3/(mol*s)
#     400 K   1.359e+09     10.1149   1.375e+10 cm^3/(mol*s)
#     500 K   8.349e+09     4.40666   3.679e+10 cm^3/(mol*s)
#     600 K   2.926e+10     2.81935   8.250e+10 cm^3/(mol*s)
#     800 K   1.545e+11     1.81455   2.803e+11 cm^3/(mol*s)
#    1000 K   4.597e+11     1.47902   6.799e+11 cm^3/(mol*s)
#    1500 K   2.430e+12     1.20398   2.926e+12 cm^3/(mol*s)
#    2000 K   6.585e+12      1.1172   7.356e+12 cm^3/(mol*s)
#   ======= =========== =========== =========== ===============
kinetics(
    label = 'OO+[H]_[H][H]+[O]O',
    kinetics = Arrhenius(
        A = (164.898, 'cm^3/(mol*s)'),
        n = 3.26753,
        Ea = (4.24828, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.57375, dn = +|- 0.059513, dEa = +|- 0.327381 kJ/mol',
    ),
)

