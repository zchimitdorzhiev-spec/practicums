def search(a, x):
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)