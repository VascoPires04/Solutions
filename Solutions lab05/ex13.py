def apaga_char(str,char):
    new = ""
    for x in str:
        if x != char:
            new += x
    return new