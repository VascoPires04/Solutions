def reconhece(str):
    value = False
    for x in str:
        if x.isdigit():value = True
        if value and not x.isdigit():return False
    return True