def explode(numero):
    if int(numero) != numero:raise ValueError("explode: argumento não inteiro")
    num = str(numero)
    y = []
    for x in num:
        y.append(int(x))
    return tuple(y)
def implode(tuplo):
    lista = list(tuplo)
    stringa = ""
    for x in lista:
        if int(x)!=x:
            raise ValueError("implode: elemento não inteiro")
        else:
            stringa += str(x)
    return 0 if stringa == "" else int(stringa)
def filtra_pares(tuplo):
    x = list(tuplo)
    return tuple([i for i in x if i%2==0])
def algarismos_pares(numero):
    if not numero: raise ValueError()
    sure = implode(filtra_pares(explode(numero)))
    return sure