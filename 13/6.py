from itertools import permutations

digits = '0123456789'

results = []

for perm in permutations(digits, 7):
    h, o, d, m, a, t = perm
    if h == '0' or m == '0':
        continue

    hod = int(h + o + d)
    mat = int(m + a + t)

    if hod * 3 == mat:
        results.append((hod, mat))

results.sort()

for hod, mat in results:
    print(f"{hod}+{hod}+{hod}={mat}")
