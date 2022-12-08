def soma_cumulativa(lista):
    if lista == []:return []
    counter = lista[0]
    new = [counter]
    for x in lista[1:]:
        counter += x
        new.append(counter)
    return new