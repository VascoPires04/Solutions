digito = 0
x = 0
str = ""
while int(digito)!=-1:
    digito = input("Escreva um dígito\n(-1 para terminar)\n? ")
    str += digito
print(f"O número é: {int(str[:-2])}")
