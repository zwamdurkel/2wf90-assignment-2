# Input:            INTEGER mod, POLY f, POLY g, POLY h
# Output:           BOOLEAN answer
# Functionality:    Return true iff (f ≡ g mod h) in Z/pZ[X].

from method.addPoly import addPoly
from method.longDivPoly import longDivPoly

def polMod(mod, x):
    y = x.copy()
    for i in range(len(y)):
        y[i] = y[i] % mod
    return y

def equalsPolyMod(mod, f, g, h):

    x = polMod(mod, f)
    x2 = x.copy()
    y = polMod(mod, g)
    z = polMod(mod, h)

    if x == y:
        return True
    if len(z) > 1 and len(f):
        x = addPoly(mod, x, z)[1]
        r = longDivPoly(mod, x, z)[3]
        while r != x2 and x != x2:
            if r == y:
                return True
            x = addPoly(mod, x, z)[1]
            r = longDivPoly(mod, x, z)[3]

    return False
#FINNEAN