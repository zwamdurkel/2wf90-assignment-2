# Input:            INTEGER mod, POLY f
# Output:           String answer
# Functionality:    Pretty print the polynomial f.
#                   This means, all coefficients get reduced modulo p and powers of X are added.
#                   E.g.: X^5 + 2X^4 + 3X^3 + 4X^2 + 5X + 6.


def displayPoly(mod, f):
    answer = ''
    for degree in range(len(f)):
        number = f[-(degree + 1)] % mod
        if number != 0 or len(f) == 1:
            if len(answer) > 0:
                answer = '+' + answer
            if degree == 1:
                answer = 'X' + answer
            if degree > 1:
                answer = 'X^' + str(degree) + answer
            if number != 1 or degree == 0:
                answer = str(number) + answer

    print('Answer:' + answer)
    return answer

# FINNEAN
