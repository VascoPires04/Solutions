def misterio(x):
    x = str(x)
    if abs(int(x[0])-int(x[-1])) <= 1:
        raise ValueError("Condições não verificadas")
    else:
        xi = x[::-1]
        xs = str(abs(int(x)-int(xi)))
        xsi = xs[::-1]
        return int(xs)+int(xsi)