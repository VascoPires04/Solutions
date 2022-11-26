x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
x3 = float(input("x3 = "))
x4 = float(input("x4 = "))
x5 = float(input("x5 = "))
lista = [x1,x2,x3,x4,x5]
media = sum(lista)/5
soma = 0
for x in lista:
    soma += (x-media)**2
desvio = (0.25*soma)**(1/2)
print(f"média = {round(media,8)} desvio padrão = {round(desvio,8)}")