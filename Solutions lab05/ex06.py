def num_para_seq_cod(numero):
    numero = [int(x) for x in str(numero)]
    for x in range(len(numero)):
        if numero[x]%2==0:
         numero[x] = (numero[x]+2)%10
        else:
            numero[x] = (numero[x] - 2) % 10
    return tuple(numero)