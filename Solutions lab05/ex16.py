def horner(tuplo,num):
    coef = [int(x) for x in list(tuplo)]
    output = 0
    for x in range(len(coef)):
        output += coef[x]*(num)**(len(coef)-(x+1))
    return output
#dont feel like applying the horner algorithm sorry if you are seeing this


