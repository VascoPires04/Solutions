def codifica(str):
    return "".join([str[x] for x in range(len(str)) if x%2==0] + [str[x] for x in range(len(str)) if x%2==1])
#desculpem a burrice na segunda parte
def descodifica(str):
    if len(str)%2==0:
        middle = len(str)//2
        even = str[:middle]
        odd = str[middle:]
        i,j=1,1
        new = ""
        while i <= len(even) or j <= len(odd):
            if i <= len(even): new += even[i-1]
            if j <= len(odd): new += odd[j-1]
            i += 1
            j += 1
        return new
    else:
        middle = (len(str) // 2)+1
        slicing = int(middle)
        even = str[:slicing]
        odd = str[slicing:]
        i, j = 1, 1
        new = ""
        while i <= len(even) or j <= len(odd):
            if i <= len(even):new += even[i-1]
            if j <= len(odd):new += odd[j-1]
            i += 1
            j += 1
        return new
