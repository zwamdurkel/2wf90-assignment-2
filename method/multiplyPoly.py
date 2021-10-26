from method.displayPoly import displayPoly

# Input:            INTEGER mod, POLY f, POLY g
# Output:           STRING answer, POLY answer-poly
# Functionality:    Compute the product f · g of polynomials f and g in Z/pZ[X].
#                   Output f · g as pretty print string and as POLY.


def multiplyPoly(mod, f, g):
    answer = [0] * (len(f) + len(g))
    # Reverse for easy for-loop
    f_rev = f[::-1]
    g_rev = g[::-1]

    # For each element in f, multiply with each element in g. Then add to answer
    for i in range(len(f)):
        for j in range(len(g)):
            answer[i + j] = (answer[i + j] + f_rev[i] * g_rev[j]) % mod

    # Reverse answer back to right order
    answer.reverse()

    # Remove unnecessary 0's
    while answer[0] == 0:
        answer.pop(0)

    return displayPoly(mod, answer), answer
