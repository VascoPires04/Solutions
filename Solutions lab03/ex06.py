lista = list(input("Escreva um inteiro\n? "))
str = ""
for x in lista:
    if int(x)%2==1:
        str+=x
if str == "":str="0"
print(f"Resultado: {str}")
