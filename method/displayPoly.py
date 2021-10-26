# Input:            INTEGER mod, POLY f
# Output:           String answer
# Functionality:    Pretty print the polynomial f.
#                   This means, all coefficients get reduced modulo p and powers of X are added.
#                   E.g.: X^5 + 2X^4 + 3X^3 + 4X^2 + 5X + 6.

def displayPoly(mod, f):
    s = ''
    i = len(f) - 1
    for x in f:
        if x != 0:
            if x != 1:
                if i == 0:
                    if i != len(f) - 1:
                        s = s + '+'
                    s = s + str(x % mod)
                    i = i - 1
                elif i == 1:
                    if i != len(f) - 1:
                        s = s + '+'
                    s = s +  str(x % mod) + 'X'
                    i = i - 1
                else: 
                    if i != len(f) - 1:
                        s = s + '+'
                    s = s +  str(x % mod) + 'X^' + str(i)
                    i = i - 1   
            else:
                if i != len(f) - 1:
                    s = s + '+'
                s = s + 'X^' + str(i)
                i = i - 1
        else:
            i = i - 1
    print('Answer:' + s)
    return s

#FINNEAN