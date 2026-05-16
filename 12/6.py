def degree5(n):
    degree = 0

    while n // 5 > 0:
        if n % 5 != 0:
            return -1
        else:
            n = n // 5
            degree += 1
    return degree

print(degree5(5))