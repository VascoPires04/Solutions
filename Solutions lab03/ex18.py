def serie_geom(r,n):
    if n < 0: raise ValueError("serie_geom: argumento incorrecto")
    c = 0
    for x in range(n+1):
        c += r**x
    return c