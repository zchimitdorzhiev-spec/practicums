def nod(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0 or b % a != 0:
        a = a % b
        if a % b == 0:
            return b
        b = b % a
        if b % a == 0:
            return a

print(nod(5, 10))