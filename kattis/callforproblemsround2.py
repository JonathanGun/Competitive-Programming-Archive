n, k = map(int, input().split())
diffs = set()
for _ in range(n):
    d = int(input())
    diffs.add(d)
x = len(diffs)
print(min(x, k))
