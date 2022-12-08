def multiplica_mat(m1,m2):
    if len(m1[0])!=len(m2):raise ValueError()
    new = []
    for i in range(len(m1)):
        current = []
        for x in range(len(m2[0])):
            counter = 0
            for j in range(len(m1[0])):
                counter += m1[i][j]*m2[j][x]
            current.append(counter)
        new.append(current)
    return new



