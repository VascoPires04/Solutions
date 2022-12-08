def ataques_rainhas(d):
    abc = "0ABCDEFGH"
    occupance = []
    for x in range(8):
        occupance.append([0]*8)
    color = ""
    for x in d:
        if d[x][1] == "rainha":
            linha = x[0]-1
            coluna = abc.index(x[1])-1
            color = d[x][0]
        else:
            occupance[x[0]-1][abc.index(x[1])-1] = [d[x][1],d[x][0],x]
    output = []
    #mesma linha
    for j in range(linha):
        element = occupance[j][coluna]
        if element != 0 and element[1]==color:
            break
        elif element != 0 :
            output.append(element)
            break
    for j in range(linha+1,8):
        element = occupance[j][coluna]
        if element != 0 and element[1]==color:
            break
        elif element != 0 :
            output.append(element)
            break
    #mesma coluna
    for j in range(coluna):
        element = occupance[linha][j]
        if element != 0 and element[1]==color:
            break
        elif element != 0:
            output.append(element)
            break
    for j in range(coluna+1,8):
        element = occupance[linha][j]
        if element != 0 and element[1]==color:
            break
        elif element != 0 :
            output.append(element)
                #mesma diagonal
    #descer(diagonal)
    current_l = linha+1
    current_c = coluna+1
    while current_l < 8 and current_c < 8:
        element = occupance[current_l][current_c]
        if element != 0 and element[1]==color:
            break
        elif element != 0:
            output.append(element)
            break
        current_l += 1
        current_c += 1
    #subir(diagonal)
    current_l = linha - 1
    current_c = coluna - 1
    while current_l >= 0 and current_c >= 0:
        element = occupance[current_l][current_c]
        if element != 0 and element[1] == color:
            break
        elif element != 0:
            output.append(element)
            break
        current_l -= 1
        current_c -= 1

    return output