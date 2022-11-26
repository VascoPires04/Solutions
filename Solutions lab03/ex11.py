numero = input("Escreva um inteiro\n? ")
previous = numero[0]
cnt=0
for x in numero[1:]:
    if x=="0" and previous=="0":cnt+=1
    previous=x
print(f"O numero tem {cnt} zeros seguidos")
