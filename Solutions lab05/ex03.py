def implode(tuplo):
    lista = list(tuplo)
    stringa = ""
    for x in lista:
        if int(x)!=x:
            raise ValueError("implode: elemento não inteiro")
        else:
            stringa += str(x)
    return int(stringa)

