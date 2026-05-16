def count(a, b):
    if a == 0 or b == 0:
        return 0
    if a == b:
        return 1
    if a > b:
        return 1 + count(a - b, b)
    return 1 + count(a, b - a)