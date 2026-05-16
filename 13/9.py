from itertools import combinations

nums = input().split()
k = int(input())

result = []
for combo in combinations(nums, k):
    result.append(' '.join(combo))

print(result)