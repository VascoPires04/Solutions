numero = 0
while numero >= 0:
    numero = int(input("Escreva um número de segundos\n(um número negativo para terminar)\n? "))
    if numero > 0 :print(f"O número de dias correspondente é {round(numero/(3600*24),8)}")