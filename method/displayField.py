# Input:            INTEGER mod, POLY modPoly, POLY a
# Output:           STRING answer, POLY answer-poly
# Functionality:    Output a representative of the field element of F that represents a,
#                   this means the unique polynomial f of degree less than the degree of q(x) that is congruent to a.
#                   Output f as pretty print string and as POLY.

from method.displayPoly import displayPoly
from method.longDivPoly import longDivPoly


def displayField(mod, modPoly, a):
    x = longDivPoly(mod, a, modPoly)[3]
    return displayPoly(mod, x), x

#FINNEAN