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
    if g == 1:
        print(1, 2)
    else:
        print(1, g)
