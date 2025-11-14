# H4 12.0 basis 6-31g

In this case there 4 electrons, 2 of each spin. For the 2-electron density
matrix we have to integrate 2 electrons out. As a result we have alpha-alpha,
alpha-beta, and beta-beta 2-electron density matrix elements. Each of these
elements are generated from multiple Slater determinant pairs (and
corresponding CI coefficient pairs).

For the unrestricted alpha-alpha pairs we have

![unrestricted alpha-alpha diagonal overview](./u_h4_12.0_6-31g_aa_d_overview.png)
![unrestricted alpha-alpha diagonal side](./u_h4_12.0_6-31g_aa_d_side.png)

The non-zero elements concentrate on 4 lines:
- For one line $d^a==1$ and $0 \le d^b \le 1$
- For the other line $d^b==1$ and $0 \le d^a \le 1$
- For one line $d^a==\textonehalf$ and $0 \le d^b \le 1$
- For the other line $d^b==\textonehalf$ and $0 \le d^a \le 1$
- There is also a line where $d^a_i = d^a_j$ and the diagonal element
  is $d^a_i d^a_j$. In this case that line almost not populated.

For the restricted alpha-alpha pairs we have

![restricted alpha-alpha diagonal](./r_h4_12.0_6-31g_aa_d.png)

In this case we see that lines where one of the occupation numbers is 1 are
missing.

For the unrestricted alpha-beta pairs we have

![unrestricted alpha-beta diagonal overview](./u_h4_12.0_6-31g_ab_d_overview.png)
![unrestricted alpha-beta diagonal side](./u_h4_12.0_6-31g_ab_d_side.png)

Now we see that the non-zero elements are concentrated on 3 lines.
- The diagonal line, which is also present in the 2-electron case
- The first two additional lines that appeared in the alpha-alpha pairs
Again some elements lie between these lines due to partial cancelation
in the 2-electron density matrix elements.

For the restricted alpha-beta pairs we have

![restricted alpha-beta diagonal overview](./r_h4_12.0_6-31g_ab_d_overview.png)
![restricted alpha-beta diagonal side](./r_h4_12.0_6-31g_ab_d_side.png)

In addition for the alpha-beta off-diagonal elements we have
for the unrestricted and restricted case respectively

![unrestricted alpha-beta off-diagonal overview](./u_h4_12.0_6-31g_ab_o.png)
![restricted alpha-beta off-diagonal overview](./r_h4_12.0_6-31g_ab_o.png)

where we see the same oval shape as for H2.

