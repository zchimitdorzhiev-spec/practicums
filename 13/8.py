from itertools import combinations

nums = input().split()
n = len(nums)

result = []
for r in range(n + 1):
    for combo in combinations(nums, r):
        result.append(' '.join(combo))

print(result)
