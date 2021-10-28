# Input:            INTEGER mod, POLY modPoly, POLY a
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the multiplicative inverse of a, i.e., the element f ∈ F such that a · f = 1
#                   (use for instance Algorithm 4.1.5, which is based on the Extended Euclidean algorithm).
#                   Output f as pretty print string and as POLY.

from method.addPoly import addPoly
from method.displayPoly import displayPoly
from method.euclidPoly import euclidPoly


def inverseField(mod, modPoly, a):
        x, y, d = euclidPoly(mod, a, modPoly)[3:6]
        if d == 1:
            return displayPoly(mod, addPoly(mod, x, d)), addPoly(mod, x, d)
        else:
            return "ERROR", []
