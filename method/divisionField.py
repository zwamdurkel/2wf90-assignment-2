# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the element f = a / b in F.
#                   Output f as pretty print string and as POLY.
from method.addPoly import addPoly
from method.displayField import displayField
from method.longDivPoly import longDivPoly
from method.displayPoly import displayPoly


def divisionField(mod, modPoly, a, b):

    x = displayField(mod, modPoly, a)[1]
    y = displayField(mod, modPoly, b)[1]

    if y == [0]:
        return 'ERROR', []

    q, r = longDivPoly(mod, x, y)[2:4]

    while r != [0]:
        x = addPoly(mod, x, modPoly)[1]
        q, r = longDivPoly(mod, x, y)[2:4]
        
    return displayPoly(mod, q), q
