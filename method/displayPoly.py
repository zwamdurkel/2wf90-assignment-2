# Input:            INTEGER mod, POLY f
# Output:           String answer
# Functionality:    Pretty print the polynomial f.
#                   This means, all coefficients get reduced modulo p and powers of X are added.
#                   E.g.: X^5 + 2X^4 + 3X^3 + 4X^2 + 5X + 6.

def displayPoly(mod, f):
    s = ''
    i = len(f)
    for x in f:
        s = s + x % mod + 'X'^i
        i = i - 1
    print(s)
    return s

#FINNEAN