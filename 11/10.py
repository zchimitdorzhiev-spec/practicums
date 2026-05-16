lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
a, b = map(int, input().split())

a -= 1
b -= 1

cut_elements = lst1[a:b+1][::-1]

lst1[a:b+1] = []

lst2.extend(cut_elements)

print(lst1)
print(lst2)