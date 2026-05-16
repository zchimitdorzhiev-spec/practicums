def count(n):
    if n // 10 == 0:
        return 1
    return 1 + count(n // 10)

print(count(18723746))