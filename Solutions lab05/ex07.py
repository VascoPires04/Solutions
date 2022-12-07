
def amigas(str1,str2):
    counter = 0
    for x in range(len(str1)):
        if str1[x] == str2[x]:
            counter += 1
    return (counter/len(str1)) >= 0.9