import random
def euromilhoes():
    output = []
    first = []
    second = []
    for x in range(5):
        first.append(random.randrange(1,50))
    output.append(first)
    for x in range(2):
        second.append(random.randrange(1,12))
    output.append(second)
    return output