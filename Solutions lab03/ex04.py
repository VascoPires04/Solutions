horas = int(input("horas de trabalho: "))
salario = int(input("salário/hora: "))
if horas <= 40:
    print(f"pagar {horas*salario}")
else:
    restante = horas-40
    print(f"pagar {(40*salario)+(restante*2*salario)}")