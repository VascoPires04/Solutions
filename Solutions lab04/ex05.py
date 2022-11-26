import math
x = float(input("Qual o valor de x\n? "))
n = float(input("Qual o valor de n\n? "))
soma = 0
for i in range(int(n)+1):
    soma += x**i/math.factorial(i)
print(f"O valor da soma é {round(soma,8)}")
