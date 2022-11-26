nota = 0
lista = []
while nota >= 0:
    nota = int(input("Nota ? "))
    if nota > 0:lista.append(nota)
c = 0
for x in lista:
    if x >= 10:c+=1
print(f"{c} positivas {round(c/len(lista)*100,8)} %")