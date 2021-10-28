# Input:            INTEGER mod, POLY f
# Output:           String answer
# Functionality:    Pretty print the polynomial f.
#                   This means, all coefficients get reduced modulo p and powers of X are added.
#                   E.g.: X^5 + 2X^4 + 3X^3 + 4X^2 + 5X + 6.


def polMod(mod, x):
    y = x.copy()
    for i in range(len(y)):
        y[i] = y[i] % mod
    return y

def displayPoly(mod, f):

    f_copy = f.copy()

    while f_copy[0] == 0 and f_copy != [0]:
        f_copy.pop(0)

    answer = ''
    for degree in range(len(f_copy)):
        number = f_copy[-(degree + 1)] % mod
        if number != 0 or len(f_copy) == 1:
            if len(answer) > 0:
                answer = '+' + answer
            if degree == 1:
                answer = 'X' + answer
            if degree > 1:
                answer = 'X^' + str(degree) + answer
            if number != 1 or degree == 0:
                answer = str(number) + answer
    
    answerpol = polMod(mod, f_copy)

    while answerpol[0] == 0 and answerpol != [0]:
        answerpol.pop(0)

    return answer, polMod(mod, f_copy)

# FINNEAN
