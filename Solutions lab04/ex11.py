def pi(x):
    i = 1
    s = 0
    while i <= x:
        if i%2==1:
            s += 1/(2*i-1)
        else:
            s-=1/(2*i-1)
        i+=1
    return s*4

