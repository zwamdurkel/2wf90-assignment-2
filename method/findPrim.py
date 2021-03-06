# Input:            INTEGER mod, POLY modPoly
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute a primitive element f in F (see Algorithm 4.4.4).
#                   Output f as pretty print string and as POLY.

from random import randint
from method.primitive import primitive
from method.displayPoly import displayPoly
from method.longDivPoly import longDivPoly


def findPrim(mod, modPoly):
    a = [0] * (len(modPoly))
    for i in range(len(a)):
        a[i] = randint(0, mod-1)
    a = longDivPoly(mod, a, modPoly)[3]
    while not primitive(mod, modPoly, a):
        a = [0] * (len(modPoly))
        for i in range(len(a)):
            a[i] = randint(0, mod-1)
        print(a)
        a = longDivPoly(mod, a, modPoly)[3]
    b = displayPoly(mod, a)[0]
    return b, a
