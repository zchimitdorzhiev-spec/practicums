def odd_list(a, n):
    if n == 0:
        return []
    if a[n - 1] % 2 == 0:
        return odd_list(a, n - 1) + [a[n - 1]]
    return odd_list(a, n - 1)