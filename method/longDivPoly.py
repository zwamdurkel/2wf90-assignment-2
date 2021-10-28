# Input:            INTEGER mod, POLY f, POLY g
# Output:           STRING answ-q, STRING answ-r, POLY answ-q-poly, POLY answ-r-poly
# Functionality:    Execute a long division to compute polynomials q,
#                   r ∈ Z/pZ[X] such that f = q · g + r in Z/pZ[X] (see e.g. Algorithm 2.2.2).
#                   Output q and r as pretty print string and as POLY, each.

from re import M
from method.addPoly import addPoly
from method.displayPoly import displayPoly
from method.subtractPoly import subtractPoly
from method.multiplyPoly import multiplyPoly

def modInv(mod, x):
    a = x
    m = mod
    x1 = 1
    x2 = 0
    while m > 0:
        q = a//m 
        r = a - q*m
        a = m
        m = r
        x3 = x1 - q * x2
        x1 = x2
        x2 = x3
    if a == 1:
        inv = x1 
    else:
        inv = "ERROR"   
    return inv

def getDegree(x):
    deg = len(x) - 1
    return deg

def longDivPoly(mod, f, g):
    q = []
    r = f.copy()
    gNew = g.copy()
    a = modInv(mod, gNew[0])
    if a == 'ERROR':
        return 'ERROR', 'ERROR', [], []
    b = [a]
    r = multiplyPoly(mod, r, b)[1]
    gNew = multiplyPoly(mod, gNew, b)[1]
    if getDegree(g) == 0:
        q = r
        r = [0]
        return displayPoly(mod, q), displayPoly(mod, r), q, r
        # v = [r[0]]
        # i = getDegree(r) - getDegree(gNew)
        # while i != 0: 
        #     v.append(0)
        #     i = i - 1
        # q = addPoly(mod, q, v)[1]
        # r = subtractPoly(mod, r, multiplyPoly(mod, v, gNew)[1])[1]
    else:       
        while getDegree(g) <= getDegree(r):
            v = [r[0]]
            i = getDegree(r) - getDegree(gNew)
            while i != 0: 
                v.append(0)
                i = i - 1
            q = addPoly(mod, q, v)[1]
            r = subtractPoly(mod, r, multiplyPoly(mod, v, gNew)[1])[1]
    for k in range(len(r)):
        r[k] = (r[k] * g[0]) % mod
    return displayPoly(mod, q), displayPoly(mod, r), q, r



#FINNEAN