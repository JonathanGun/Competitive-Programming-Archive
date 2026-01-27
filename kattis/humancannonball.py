from math import hypot


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
n = int(input())

pts = [(x1, y1), (x2, y2)] + [tuple(map(float, input().split())) for _ in range(n)]


def dist(i, j):
    return hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])


def time(i, j):
    d = dist(i, j)
    if i < 2:
        return d / 5
    return 2 + abs(d - 50) / 5


d = [[time(i, j) for j in range(n + 2)] for i in range(n + 2)]

for k in range(n + 2):
    for i in range(n + 2):
        for j in range(n + 2):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(f"{d[0][1]:.6f}")
