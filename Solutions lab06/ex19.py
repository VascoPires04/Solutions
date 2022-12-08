def computeGCD(x,y):
    gcd = 0
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i

    return gcd
def cria_racional(first,second):
    if isinstance(first,int) and isinstance(second,int) and second!=0:
        sure = computeGCD(abs(first),abs(second))
        one = abs(second)//sure
        two = abs(first)//sure if (second > 0 and first > 0) or (second < 0 and first < 0) else -(abs(first)//sure)
        return {"d" : one, "n" : two}
    elif second == 0:
        raise ValueError("o denominador não pode ser 0")
    else:
        raise ValueError("os números devem ser inteiros")
def escreve_racional(dic):
    dic = cria_racional(dic["n"],dic["d"])
    n = dic["n"]
    d = dic["d"]
    print(f"{n}/{d}")
    return n,d
def soma_racionais(d1,d2):
   n1,d1 = map(int,escreve_racional(d1))
   n2,d2 = map(int,escreve_racional(d2))
   ntotal = 0
   dtotal = 0
   if d1==d2:
       dtotal = d1
       ntotal = n1+n2
   else:
       n1 = d2*n1
       n2 = d1*n2
       dtotal = d1*d2
       ntotal = n1+n2
   return {"d" : dtotal, "n" : ntotal}

print(soma_racionais({'d': 6, 'n': 4},{'d': 3, 'n': 2}))