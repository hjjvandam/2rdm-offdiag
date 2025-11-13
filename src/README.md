# Calculator for 2RDM off-diagonal elements

Ultimately we want to plot real 2RDM off-diagonal elements as a function of
occupation numbers (i.e. eigenvalues of the 1RDM). The basic approach is
to

- perform an SCF calculation
- perform a Full-CI calculation
- calculate the 1RDM
- diagonalize the 1RDM
- calculate the natural orbitals
- perform a Full-CI calculation in the natural orbital basis
- calculate the 1RDM and the 2RDM
- extract the relevant triples of occupation numbers and 2RDM matrix elements

To plot the results I plan to use a tool like GnuPlot. The first question
is how to store the results so GnuPlot can plot them? It looks like the right
function to use is `splot` as in `splot "data.txt" with points`. Where
`data.txt` is a file where every line defines a point with `x y z` where
`z=f(x,y)`. Here `f(x,y)` is not explicitly known but we attempt to get an
impression of what it looks like.

The code is a Python script that uses PySCF for the ab-initio calculations.
The script takes a molecular structure in an XYZ file, a basis set, a charge,
and a number of open shell orbitals as inputs. The default values for the
charge and the number of open shell orbitals are both 0 unless the number of
electrons for the specified charge is odd. In that case the default number of
open shells will be 1.

It turns out that the results are rather different using Unrestricted Full-CI
versus Restricted Full-CI. The unrestricted version can generate spin broken
solutions, with rather different occupation numbers. Hence I have created
two different versions of the script. One that performs Restricted Full-CI
calculations where the wavefunction is restricted to singlet states. Another
one that performs Unrestricted Full-CI calculations without spin restrictions.
Note also that when repeating the Full-CI calculation in the natural orbital
basis you have to make sure that the code finds the same state again. I found
that the Full-CI code has to calculate multiple states to have a good chance of
finding the same state again.
