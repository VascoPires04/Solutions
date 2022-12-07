def explode(numero):
    if int(numero) != numero:raise ValueError("explode: argumento não inteiro")
    num = str(numero)
    y = []
    for x in num:
        y.append(int(x))
    return tuple(y)