# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the element f = a / b in F.
#                   Output f as pretty print string and as POLY.
from method.euclidPoly import longDiv
from method.longDivPoly import longDivPoly
from method.displayPoly import displayPoly


def divisionField(mod, modPoly, a, b):
    answer = longDivPoly(mod, longDiv(mod, a, b)[1], modPoly)[3]
    return displayPoly(mod, answer), answer
