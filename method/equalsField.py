# Input:            INTEGER mod, POLY modPoly, POLY a, POLY b
# Output:           BOOLEAN answer
# Functionality:    Test if a = b in F. Output true iff (a = b in F).

from method.addPoly import addPoly
from method.displayField import displayField
from method.longDivPoly import longDivPoly


def equalsField(mod, modPoly, a, b):

    x = displayField(mod, modPoly, a)[1]
    y = displayField(mod, modPoly, b)[1]

    if x == y:
        return True

    x = addPoly(mod, x, modPoly)[1]
    r = longDivPoly(mod, x, modPoly)[3]

    while r != a:
        x = addPoly(mod, x, modPoly)[1]
        r = longDivPoly(mod, x, modPoly)[3]
        if r == y:
            return True
    return False
