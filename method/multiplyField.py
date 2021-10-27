# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the element f = a · b in F.
#                   Output f as pretty print string and as POLY.
from method.multiplyPoly import multiplyPoly
from method.longDivPoly import longDivPoly
from method.displayPoly import displayPoly


def multiplyField(mod, modPoly, a, b):
    answer = longDivPoly(mod, multiplyPoly(mod, a, b)[1], modPoly)[3]
    return displayPoly(mod, answer), answer