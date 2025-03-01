n, m, k = map(int, input().split())

if k == n*m:
    print(0)
elif k % n == 0 or k % m == 0:
    print(1)
else:
    