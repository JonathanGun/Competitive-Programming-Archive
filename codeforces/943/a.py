from math import gcd

n = int(input())

for _ in range(n):
    x = int(input())
    mx = 0
    ans = 0
    for y in range(1, x):
        tmp = gcd(x, y) + y
        # print(y, tmp)
        if tmp > mx:
            mx = tmp
            ans = y
    print(y)
