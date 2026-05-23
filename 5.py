def count_descendants(parent, tree):
    total = 0
    if parent in tree:
        for child in tree[parent]:
            total += 1 + count_descendants(child, tree)
    return total

n = int(input())
tree = {}

for _ in range(n):
    parent, child = input().split()
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

target = input()
result = count_descendants(target, tree)
print(result)
