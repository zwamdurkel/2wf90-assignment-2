# Input:            INTEGER mod, POLY modPoly
# Output:           2D STRING ARRAY answer, 2D POLY ARRAY answer-poly
# Functionality:    Generate the full multiplication table of F. Return it once with elements pretty printed and
#                   once with elements as POLY’s.
#                   In final format, the output is supposed to be a sequence of rows (see examples).

from method.multiplyField import multiplyField
from method.displayPoly import displayPoly


def multTable(mod, modPoly):
    answer = [[0] * pow(mod, (len(modPoly)-1)) for i in range(pow(mod, (len(modPoly)-1)))]
    answer2 = [["0"] * pow(mod, (len(modPoly)-1)) for i in range(pow(mod, (len(modPoly)-1)))]
    axis = [0] * pow(mod, (len(modPoly)-1))
    for i in range(pow(mod, (len(modPoly)-1))):
        poly = [0] * (len(modPoly)-1)
        length = i
        j = (len(modPoly)-1)
        while length >= mod:
            j -= 1
            poly[j] = length%mod
            length = int((length - poly[j]) / mod)
        if(not length == 0):
            poly[j-1] = length    
        axis[i] = poly
    print(axis)
    for i in range(pow(mod, (len(modPoly)-1))):
        for j in range(pow(mod, (len(modPoly)-1))):
            answer[i][j] = multiplyField(mod, modPoly, axis[i],axis[j])[1]
    print(answer)
    for i in range(pow(mod, (len(modPoly)-1))):
        for j in range(pow(mod, (len(modPoly)-1))):
            answer2[i][j] = displayPoly(mod, answer[i][j])[0]
    return answer2, answer
