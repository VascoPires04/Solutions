def soma_mat(m1,m2):
    for i in range(len(m1)):
        for x in range(len(m1[i])):
            m1[i][x] += m2[i][x]
    return m1