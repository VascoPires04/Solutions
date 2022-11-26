segundos = int(input("Escreva o número de segundos "))
dias = segundos//(3600*24)
restante1 = segundos - (dias*3600*24)
horas = restante1//3600
restante2 = restante1 - (horas*3600)
minutos = restante2//60
segundos = restante2 - minutos*60
print(f"dias: {dias} horas: {horas} mins: {minutos} segs: {segundos}")