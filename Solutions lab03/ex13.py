string=""
for x in range(1,10):
    string+=str(x)
    x_inicial = x
    x = int(string)
    print(f"{x} x 8 + {x_inicial} = {x*8+x_inicial}")