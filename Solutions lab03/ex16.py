def bissexto(x):
    if x % 4 == 0:
        if x % 100 != 0 or x % 400 == 0:
            return True
        else:
            return False
    else:
        return False