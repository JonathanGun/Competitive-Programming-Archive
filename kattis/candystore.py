from collections import defaultdict

n, q = map(int, input().split())

cnt = defaultdict(list)
for _ in range(n):
    a, b = input().split()
    cnt[a[0] + b[0]].append(a + " " + b)

for _ in range(q):
    x = cnt[input()]
    if len(x) == 0:
        print("nobody")
    elif len(x) == 1:
        print(x[0])
    else:
        print("ambiguous")
