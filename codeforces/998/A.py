n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    x1 = ls[0] + ls[1]
    x2 = ls[2] - ls[1]
    x3 = ls[3] - ls[2]
    cnt = len(set([x1, x2, x3]))
    print(4 - cnt)
