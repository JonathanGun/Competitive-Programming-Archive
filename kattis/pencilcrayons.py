from collections import Counter

n, k = map(int, input().split())

ans = 0
for _ in range(n):
    for k, v in Counter(input().split()).items():
        ans += max(0, v - 1)
print(ans)
