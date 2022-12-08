def calc_F(i,h,p):
    return 655 + 4.3 * p + 4.7 * h + 4.7 * i
def calc_M(i,h,p):
    return 66 + 6.3 * p + 12.9 * h + 6.8 * i
def metabolismo(dic):
    new = {}
    for x in dic:
        if dic[x][0]=="F": new[x] = calc_F(dic[x][1],dic[x][2],dic[x][3])
        else: new[x] = calc_M(dic[x][1], dic[x][2], dic[x][3])
    return new