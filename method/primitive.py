# Input:            INTEGER mod, POLY modPoly, POLY a
# Output:           BOOLEAN answer
# Functionality:    Verify if a is a primitive element in F. Output true iff (a is primitive in F).

import math
from method.multiplyPoly import multiplyPoly
from method.longDivPoly import longDivPoly

def primeFactors(n):

    factors = []
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            factors.append(int(i))
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(int(n))

    return factors

def primitive(mod, modPoly, a):
    i = 0

    q = mod ** (len(modPoly) - 1)

    factors = primeFactors(q-1)
    unique_factors = list(set(factors))

    while i < len(unique_factors) and longDivPoly(mod, powerPoly(mod, a, (q-1)/unique_factors[i]), modPoly)[3] != [1]:
        i += 1
    
    return False if i < len(unique_factors) else True

def powerPoly(mod, a, power):
    a_copy = a.copy()

    for i in range(1,int(power)):
        a_copy = multiplyPoly(mod, a_copy, a)[1]
    
    return a_copy

