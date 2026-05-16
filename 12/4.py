def sum_progress(a1, r, n):
    return sum_progress(a1, r, n) + sum_progress(a1, r, n - 1)

print(sum_progress(1, 3, 3))