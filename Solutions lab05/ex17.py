def trapz(x,y):
    counter = 0
    x = list(x)
    y = list(y)
    for i in range(1,len(x)):
        counter += (y[i-1]+y[i])*(x[i]-x[i-1])/2
    return counter
