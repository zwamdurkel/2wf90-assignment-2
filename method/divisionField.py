# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the element f = a / b in F.
#                   Output f as pretty print string and as POLY.
from method.addPoly import addPoly
from method.euclidPoly import longDiv
from method.longDivPoly import longDivPoly
from method.displayPoly import displayPoly


def divisionField(mod, modPoly, a, b):
    if b == [0]:
        return 'ERROR', []

    q, r = longDivPoly(mod, a, b)[2:4]

    while r != [0]:
        a = addPoly(mod, a, modPoly)[1]
        q, r = longDivPoly(mod, a, b)[2:4]
        
    return displayPoly(mod, q), q
