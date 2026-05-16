lst = list(map(int, input().split()))
command = input().strip()

direction = command[0]
k = int(command[1:])

k = k % len(lst)

if direction == 'R':
    lst = lst[-k:] + lst[:-k]
elif direction == 'L':
    lst = lst[k:] + lst[:k]

print(lst)