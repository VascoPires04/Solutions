import math
def seno(x,i):
    s = 0
    for n in range(2*i+2):
        s += ((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
    return s
