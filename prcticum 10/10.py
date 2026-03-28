def print_numbers_with_allowed_digits(A, B):
    allowed_digits = {'1', '3', '4', '8', '9'}

    if not isinstance(A, int) or not isinstance(B, int):
        return

    if A > B:
        A, B = B, A

    for num in range(A, B + 1):
        num_str = str(num)

        valid = True
        for digit in num_str:
            if digit not in allowed_digits:
                valid = False
                break

        if valid:
            print(num, end=' ')


print_numbers_with_allowed_digits(4, 100)
print_numbers_with_allowed_digits(100, 4)