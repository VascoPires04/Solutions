def logn(x,n):
    soma = 0
    for k in range(n):
        soma += (1/(2*k+1))*(((x-1)/(x+1))**(2*k+1))
    return 2*soma