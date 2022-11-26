import math
def arco_seno(x,i):
    s = 0
    for n in range(2*i+2):
        first = math.factorial(2*n)/(2**n*math.factorial(n))**2
        second = (x**(2*n+1))/(2*n+1)
        s+=(first*second)
    return s
