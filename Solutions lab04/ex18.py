import math
def coseno(x,i):
    s = 0
    for n in range(2*i+1):
        s += ((-1)**n)*(x**(2*n))/math.factorial(2*n)
    return s