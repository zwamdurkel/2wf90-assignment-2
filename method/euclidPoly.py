# Input:            INTEGER mod, POLY f, POLY g
# Output:           STRING answ-a, STRING answ-b, STRING answ-d, POLY answ-a-poly, POLY answ-b-poly, POLY answ-d-poly
# Functionality:    execute the extended Euclidean algorithm to compute polynomials a, b, d∈Z/pZ[X]
#                   such that af + bg = d = gcd(f, g) in Z/pZ[X].
#                   Remember, that we defined the gcd to be monic, i.e.,
#                   the leading coefficient has to be 1 (seeAlgorithms 2.2.10).
#                   Output a, b, and d as pretty print string and as POLY, each.

from method.addPoly import addPoly
from method.displayPoly import displayPoly
from method.longDivPoly import getDegree, longDivPoly, modInv
from method.multiplyPoly import multiplyPoly
from method.subtractPoly import subtractPoly

def euclidPoly(mod, f, g):
    a = f.copy()
    b = g.copy()
    x = [1]
    v = [1]
    y = [0]
    u = [0]
    while b != [0]:
        q, r = longDivPoly(mod, a, b)[2:4]
        a = b
        b = r
        x2 = x
        y2 = y
        x = u
        y = v
        u = subtractPoly(mod, x2, multiplyPoly(mod, q, u)[1])[1]
        v = subtractPoly(mod, y2, multiplyPoly(mod, q, v)[1])[1]
    a = multiplyPoly(mod, x, [modInv(mod, f[0])])[1]
    b = multiplyPoly(mod, y, [modInv(mod, f[0])])[1]
    d = addPoly(mod, multiplyPoly(mod, x, f)[1], multiplyPoly(mod, y, g)[1])[1]
    if getDegree(d) == 0:
        a = multiplyPoly(mod, a, [modInv(mod, d[0])])[1]
        b = multiplyPoly(mod, b, [modInv(mod, d[0])])[1]
        d = [1]
    return (
    displayPoly(mod, a), 
    displayPoly(mod, b),
    displayPoly(mod, d), 
    a, b, d
    )
