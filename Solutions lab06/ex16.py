def conta_palavras(str):
    used = []
    dic = {}
    for x in str.split(" "):
        if x not in used:
            dic[x] = str.split(" ").count(x)
    return dic
def mostra_ordenado(dic):
    new = {}
    for i in sorted(dic.keys()):
        new[i] = dic[i]
    for x in new:
        print(f"{x} {new[x]}")