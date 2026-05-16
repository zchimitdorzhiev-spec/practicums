set1 = set(input().split())
set2 = set(input().split())
value = input()

if value in set1 and value in set2:
    print("YES")
else:
    print("NO")