def variance(x):
    x = list(x)
    counter = 0
    media = sum(x)/len(x)
    for i in range(0,len(x)):
        counter += (x[len(x)-(i+1)]-media)**2
    return 1/(len(x)-1)*counter