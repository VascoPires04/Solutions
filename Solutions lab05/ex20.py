def closest(x,num):
    x = list(x)
    closer = 0
    dif = 10000
    for i in x:
        if abs(i-num) < dif:
            closer = i
            dif = abs(i-num)
    return closer