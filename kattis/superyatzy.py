from collections import Counter
n, m = map(int, input().split())
cnts = Counter()
for _ in range(n):
    x = int(input())
    cnts[x] += 1
if max(cnts.values()) + m >= n:
    print("Ja")
else:
    print("Nej")
