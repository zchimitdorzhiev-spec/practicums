def combin(n, k):
    if k == 0 or k == n:
        return 1
    if k < 0 or k > n:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)