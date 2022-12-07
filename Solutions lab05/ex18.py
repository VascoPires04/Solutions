import math
def interpol(x,y,num):
    x = list(x)
    y = list(y)
    first = 0
    second = 0
    for i in range(1,len(x)):
        if num >= x[i-1] and num <= x[i]:
            first += i-1
            second += i
            break
    if first == 0 and second == 0:
        return math.nan
    value = y[first] + (num - x[first])*((y[second]-y[first])/(x[second]-x[first]))
    return value