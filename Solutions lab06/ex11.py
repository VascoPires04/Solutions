def agrupa_por_chave(lista):
    dic = {}
    for x in lista:
        if x[0] not in dic:
            dic[x[0]] = [x[1]]
        else:
            dic[x[0]].append(x[1])
    return dic