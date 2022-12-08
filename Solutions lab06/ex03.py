def elemento_matriz(m,i,j):
    if i < len(m) and j < len(m[i]): return m[i][j]
    raise ValueError(f"elemento_matriz: indice invalido, coluna {j}")