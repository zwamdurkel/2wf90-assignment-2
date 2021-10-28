# Input:            INTEGER mod, INTEGER deg
# Output:           STRING answer, POLY answer-poly
# Functionality:    Find an irreducible polynomial f ∈ Z/pZ[X] of degree n.
#                   Output f as pretty print string and as POLY.

from random import randint
from method.irreducible import irreducible
from method.displayPoly import displayPoly


def findIrred(mod, deg):
    a = [0] * (len(deg)+1)
    for i in a:
        a[i] = randint(0,mod-1)
    while not irreducible(mod, a):
        for i in a:
            a[i] = randint(0,mod-1)
    b = displayPoly(mod, a)[1]
    return b, a
