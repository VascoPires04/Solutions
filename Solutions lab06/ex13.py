def resumo_fp(notas_dict):
    aprovados,reprovados,notas=0,0,0
    for x in notas_dict:
        if x >= 10:
            aprovados += len(notas_dict[x])
            notas += (x*len(notas_dict[x]))
        else:
            reprovados += len(notas_dict[x])
    return (notas/aprovados,reprovados)