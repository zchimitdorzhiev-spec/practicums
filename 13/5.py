n = int(input())

sieve = set(range(2, n))
for i in range(2, int(n ** 0.5) + 1):
    if i in sieve:
        sieve -= set(range(i * i, n, i))

primes = sorted(sieve)
print(*primes)