# Input:            INTEGER mod, POLY f
# Output:           BOOLEAN answer
# Functionality:    Return true iff f is irreducible in Z/pZ[X]
from method.euclidPoly import euclidPoly
def irreducible(mod, f):
    t = 1
    poly = [0] * mod
    poly[0] =  mod-1
    for i in range(mod-2):
        poly[i+1] = 0
    poly[mod-1] = 1
    while euclidPoly(mod, f, poly)[5] == 1:
        t += 1
        poly[0] =  mod-1
        for i in range(pow(mod,t)-2):
            poly[i+1] = 0
        poly[mod-1] = 1
    if(t == len(f)-1):
        return True
    return False
