import math
pi = math.pi
def area_circulo(r):
    return round(pi*(r**2),8) if r >= 0 else 0
def area_coroa(r1,r2):
    if r1 > r2:raise ValueError("r1 > r2")
    return area_circulo(r2)-area_circulo(r1)