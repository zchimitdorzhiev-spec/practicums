def print_fibonacci(n):
    if n <= 0:
        print("Количество чисел должно быть положительным")
        return

    a, b = 1, 1

    if n >= 1:
        print(a, end=" ")
    if n >= 2:
        print(b, end=" ")

    for i in range(2, n):
        next_num = a + b
        print(next_num, end=" ")
        a, b = b, next_num

    print()


print_fibonacci(5)