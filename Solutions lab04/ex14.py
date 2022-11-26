def euler(f,y0,t0,tn,n):
    h = (tn-t0)/n
    for i in range(n):
        y0 = y0 + f(t0,y0)*h
    return y0