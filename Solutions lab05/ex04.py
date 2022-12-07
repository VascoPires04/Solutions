def filtra_pares(tuplo):
    x = list(tuplo)
    return tuple([i for i in x if i%2==0])