def divisores(i):
    if i < 0 or str(i).count(".")>0:raise ValueError("wrong")
    c = 0
    for x in range(2,int(i**(1/2))+1):
        if i%x==0:c+=1
    if int(i**(1/2)) == i**(1/2):return c*2-1
    else:return c*2
