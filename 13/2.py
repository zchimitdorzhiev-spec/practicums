n = int(input())
common_courses = set(input().split())
for _ in range(n - 1):
    common_courses &= set(input().split())
print(len(common_courses))
print(common_courses)