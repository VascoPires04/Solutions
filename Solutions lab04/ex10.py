import math
#10 a)
def valor(q,j,anos):
    if j <= 0 or j >= 1 or anos < 0:raise ValueError()
    return q*((1+j)**anos)
#10 b)
def duplicar(q,j):
    return math.ceil(1/math.log(1+j,2))