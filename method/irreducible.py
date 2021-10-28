# Input:            INTEGER mod, POLY f
# Output:           BOOLEAN answer
# Functionality:    Return true iff f is irreducible in Z/pZ[X]
from method.euclidPoly import euclidPoly
def irreducible(mod, f):
    t = 1
    poly = [0] * (mod + 1)
    poly[-1] =  0
    poly[-2] =  mod-1
    for i in range(mod-3):
        poly[-(i+2)] = 0
    poly[0] = 1
    while euclidPoly(mod, f, poly)[5] == [1]:
        t += 1
        poly = [0] * pow(mod + 1,t)
        poly[-1] =  0
        poly[-2] =  mod-1
        for i in range(pow(mod + 1,t)-2):
            poly[-(i+2)] = 0
        poly[0] = 1
    if(t == len(f)-1):
        return True
    return False
