def seq_racaman(n):
    arr = [0] * n
    arr[0] = 0
    for i in range(1, n):
        curr = arr[i - 1] - i
        for j in range(0, i):
            if ((arr[j] == curr) or curr < 0):
                curr = arr[i - 1] + i
                break
        arr[i] = curr
    return arr