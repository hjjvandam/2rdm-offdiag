# Comparisons across data sets

In this README document we compare results between data sets, for example, how data sets
change with the density of hydrogen atoms, or how the data sets change with the number
of hydrogen atoms (and therefore the number of electrons). Comparisons between
closed shell and unrestricted open shell formulations are made in each of sub-directories.

# Comparing different densities

## H2 cases

The H2 cases involve 2-electron systems for which the equations can be solved largely
analytically. In particular there is only alpha-beta correlation as there are no
alpha-alpha nor beta-beta pairs.

For the restricted calculations we see for the diagonal elements

![restricted alpha-beta diagonal](./r_h2_xx.0-6-31g_ab_d_1.png)

and for the off-diagonal elements

![restricted alpha-beta off-diagonal](./r_h2_xx.0-6-31g_ab_o_1.png)

For the unrestricted calculations we see for the diagonal elements

![unrestricted alpha-beta diagonal](./u_h2_xx.0-6-31g_ab_d_1.png)

and for the off-diagonal elements

![unrestricted alpha-beta off-diagonal](./u_h2_xx.0-6-31g_ab_o_1.png)

From this we see a few things:
- In general for the 2-electron systems the density does not seem to affect
  the results much, even though the the total energies should
- Only in the lowest density case there are some deviations:
  - in the restricted case there are "stems" in the diagonal and off-diagonal elements
    at the lowest density which disappear at higher densities
  - in the unrestricted case there a few points with the lowest density
    that disappear at higher densities
- the artifacts above seem to relate to uncorrelated electrons as they only
  occur at low atom/electron densities
