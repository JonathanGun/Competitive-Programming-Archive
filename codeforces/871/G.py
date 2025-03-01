ROW = 2023
MAXN = ROW * ROW
cost = [0 for i in range(MAXN)]

cur = 0
for row in range(1, ROW + 1):
    for i in range(row):
        cur += 1
        cost[cur] = cur * cur
        if row == 1:
            continue
        topLeft = cur - row
        topRight = cur - row + 1
        topTop = cur - 2 * row + 2
        if i != 0:
            cost[cur] += cost[topLeft]
        if i < row - 1:
            cost[cur] += cost[topRight]
        if row > 1 and i != 0 and i < row - 1:
            cost[cur] -= cost[topTop]

t = int(input())
for _ in range(t):
    n = int(input())
    print(cost[n])
