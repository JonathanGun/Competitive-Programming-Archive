n = int(input())
cur, mn = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    cur += b - a
    if cur > mn:
        mn = cur
print(mn)
