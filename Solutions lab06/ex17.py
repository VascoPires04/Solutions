def soma_dicionarios(d1,d2):
    for x in d2:
        if x not in d1:
            d1[x] = d2[x]
        else:
            for i in d2[x]:
                if i not in d1[x]:
                    d1[x].append(i)
            d1[x] = sorted(d1[x])
    return d1
