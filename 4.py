n = int(input())
dictionary = {}

for _ in range(n):
    parts = input().split()
    form = parts[0]
    items = parts[1:]
    for item in items:
        dictionary[item] = form

target = input()
result = dictionary.get(target, target)

print(result)
