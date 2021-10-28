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
    for i in a:
        a[i] = randint(0,mod-1)
    longDivPoly(mod, a, modPoly)[3]
    while not primitive(mod, a):
        for i in a:
            a[i] = randint(0,mod-1)
        longDivPoly(mod, a, modPoly)[3]
    b = displayPoly(mod, a)[1]
    return b, a

#FINNEAN