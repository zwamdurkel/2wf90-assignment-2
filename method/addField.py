# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the element f = a + b in F.
#                   Output f as pretty print string and as POLY.

from method.addPoly import addPoly
from method.longDivPoly import longDivPoly
from method.displayPoly import displayPoly


def addField(mod, modPoly, a, b):
    answer = longDivPoly(mod, addPoly(mod, a, b)[1], modPoly)[3]
    return displayPoly(mod, answer)[0], answer

#(verbeterd door) FINNEAN