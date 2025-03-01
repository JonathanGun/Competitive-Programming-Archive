from collections import defaultdict

n = int(input())
views = defaultdict(int)
for _ in range(n):
    name, r = input().split()
    r = int(r)
    views[name] += r
print(max(views, key=views.get))
