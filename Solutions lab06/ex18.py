def mais_antigo(lista):
    antigo = ""
    anos = 100000
    for x in range(len(lista)):
        if lista[x]["ano"] < anos:
            antigo = lista[x]["titulo"]
            anos = lista[x]["ano"]
    return antigo