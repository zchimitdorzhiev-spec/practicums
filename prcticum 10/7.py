def print_common_multiples_simple(A, B, N):
    start = max(A, B)

    found = False
    for num in range(start, N + 1):
        if num % A == 0 and num % B == 0:
            print(num, end=" ")
            found = True

    if not found:
        print("нет общих кратных")


print_common_multiples_simple(3, 5, 50)