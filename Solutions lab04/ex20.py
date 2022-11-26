def arctan(x,i):
    s = 0
    first_term = x/(1+x**2)
    for n in range(2*i+1):
        p = 1
        for k in range(1,n+1):
            p*=(2*k*x**2)/((2*k+1)*(1+x**2))
        s+=p
    return s*first_term
