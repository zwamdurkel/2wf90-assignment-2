# Input:            INTEGER mod, POLY f, POLY g
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the difference f − g of polynomials f and g in Z/pZ[X].
#                   Output f − g as pretty print string and as POLY.

from method.displayPoly import displayPoly


def subtractPoly(mod, f, g):
    answer = []

    # Subtract elementwise mod( mod )
    for i in range(1, max(len(f), len(g)) + 1):
        numF = f[-i] if i <= len(f) else 0
        numG = g[-i] if i <= len(g) else 0
        numAnswer = (numF - numG) % mod
        answer.insert(0, numAnswer)

    # Remove unnecessary 0's
    while answer[0] == 0 and answer != [0] :
        answer.pop(0)

    return displayPoly(mod, answer)[0], answer
