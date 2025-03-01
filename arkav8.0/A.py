from collections import defaultdict
from math import comb, prod

n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    m, _ = map(int, input().split())
    cnt[m] += 1

print(prod(cnt.values()) * comb(len(cnt), 2))
