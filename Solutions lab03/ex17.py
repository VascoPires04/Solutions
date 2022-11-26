def bissexto(x):
    if x % 4 == 0:
        if x % 100 != 0 or x % 400 == 0:
            return True
        else:
            return False
    else:
        return False
def dias_mes(mes,ano):
    dic = {"jan":31, "fev":28,"mar":31,"abr":30,"mai":31,"jun":30,"jul":31,"ago":31,"set":30,"out":31,"nov":30,"dez":31}
    if mes not in dic: raise ValueError("Mês não existe")
    else:
        if bissexto(ano) and mes=="fev":
            return dic[mes]+1
        else:
            return dic[mes]