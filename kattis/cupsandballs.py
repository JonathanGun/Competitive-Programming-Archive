g = int(input())
n = int(input())

cur = 2
for _ in range(n):
    a, b = map(int, input().split())
    if a == cur:
        cur = b
    elif b == cur:
        cur = a
if cur == g:
    for i in range(1, 4):
        if i != g:
            print(i, end=" ")
    print()
else:
    print(cur, g)
