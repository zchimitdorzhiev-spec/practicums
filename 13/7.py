from itertools import permutations

nums = input().split()
perms = sorted(set(permutations(nums)))

for p in perms:
    print(' '.join(p))