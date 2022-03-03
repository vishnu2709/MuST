*****************
About
*****************

**MuST** is a research project supported by National Science Fundation to build
a public ab initio electronic structure calculation software package,
with petascale and beyond computing capability, for the first principles
study of quantum phenomena in disordered materials. The MuST package is now
(as of January 1st, Year 2020) free to download on GitHub (https://github.com/mstsuite/MuST.git)
under a BSD 3-clause license.

MuST is developed based on full-potential multiple scattering theory, also
known as Korringa-Kohn-Rostoker method, with Green function approach. It is
built upon decades of development of research codes led by Malcolm Stocks, and
his postdocs and students, in the Theory Group of Metals and Ceramics Division,
which later became Materials Science and Technology Division, in Oak Ridge National
Laboratory. The original research codes include Korringa-Kohn-Rostoker Coherent
Potential Approximation (KKR-CPA), a highly efficient ab initio method for the
study of random alloys, and Locally Self-consistent Multiple Scattering (LSMS)
method, a linear scaling ab initio code capable of treating extremely large
disordered systems from the first principles using the largest parallel supercomputers
available. It is originally suggested by Mark Jarrell, and also shown by model calculations,
that strong disorder and localization effects can also be studied within the LSMS
formalism with cluster embedding in an effective medium with the Typical Medium
Dynamical Cluster Approximation (TMDCA), which enables a scalable approach for first
principles studies of quantum materials.

The ultimate goal of MuST project is to provide a computational framework for
the investigation of quantum phase transitions and electron localization in the
presence of disorder in real materials, and enable the computational study of
local chemical correlation effects on the magnetic structure, phase stability,
and mechanical properties of solid state materials with complex structures.

Ther starting point of the MuST package is the integration of two research codes: LSMS
(formerly LSMS3) and MST (formerly MST2), both are originally based on the legacy LSMS-1
code developed in the mid of 1990s in Oak Ridge National Laboratory.

The LSMS code, maintained by Markus Eisenbach, is mainly written in C++. It consists
of muffin-tin LSMS with an interface for Monte-Carlo simulation driver. The LSMS code
is one of the baseline benchmark codes for DoE COREL systems and has also been selected as
one of the CAAR projects for exascale computing on Frontier system. The LSMS code demonstrates
nearly ideal linear scaling with 96% parallel scaling efficiency across the Titan machine
at ORNL.

The MST code, maintained by Yang Wang, is mainly written in FORTRAN 90. It focuses on physics
capabilities, and in the mean time serves as a platform for implementing and testing full-
potential multiple scattering theory and its numerical algorithms. It consists of LSMS, KKR,
and KKR-CPA codes and is capable of performing 1) muffin-tin and full-potential;
2) non-relativistic, scalar-relativistic, and fully-relativistic; and 3) non-spin-polarized,
spin-polarized, and spin-canted ab initio electronic structure calculations.

The KUBO code, maintained by Vishnu Raghuraman, is mainly written in FORTRAN 90. It implements
the Kubo-Greenwood formula in the framework of KKR-CPA method and calculates the electrical
conductivity of random alloys.
