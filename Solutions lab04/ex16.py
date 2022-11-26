import math
def expon(x,n):
    soma = 0
    for i in range(n+1):
        soma += x ** i / math.factorial(i)
    return soma