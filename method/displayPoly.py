# Input:            INTEGER mod, POLY f
# Output:           String answer
# Functionality:    Pretty print the polynomial f.
#                   This means, all coefficients get reduced modulo p and powers of X are added.
#                   E.g.: X^5 + 2X^4 + 3X^3 + 4X^2 + 5X + 6.

def displayPoly(mod, f):
    s = ''
    i = len(f)
    for x in f:
        if x != 0:
            if x != 1:
                s = s + str(x % mod) + 'X^' + str(i) + ' '
                i = i - 1
            else:
                s = s + 'X^' + str(i) + ' '
                i = i - 1
    print('Answer:' + s)
    return s

#FINNEAN