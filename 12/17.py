def function1(x):
    def is_prime_recursive(n, divisor):
        if divisor * divisor > n:
            return 1
        if n % divisor == 0:
            return 0
        return is_prime_recursive(n, divisor + 1)

    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    return is_prime_recursive(x, 3)