r, c = map(int, input().split())

filled = [[False for j in range(c)] for i in range(r)]
def floodfill(i, j):
    if filled[i][j]:
        return
    if grid[i][j] == "W":
        return
    filled[i][j] = True
    if i > 0 and not filled[i-1][j]:
        floodfill(i-1, j)
    if i < r - 1 and not filled[i+1][j]:
        floodfill(i+1, j)
    if j > 0 and not filled[i][j-1]:
        floodfill(i, j-1)
    if j < c - 1 and not filled[i][j+1]:
        floodfill(i, j+1)

grid = []
for _ in range(r):
    grid.append(list(input()))

cnt = 0
for i in range(r):
    for j in range(c):
        if not filled[i][j] and grid[i][j] == "L":
            floodfill(i, j)
            cnt += 1
print(cnt)
