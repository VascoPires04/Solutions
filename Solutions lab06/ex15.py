def conta_palavras(str):
    used = []
    dic = {}
    for x in str.split(" "):
        if x not in used:
            dic[x] = str.split(" ").count(x)
    return dic