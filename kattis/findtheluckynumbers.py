r, c = map(int, input().split())
s = int(input())

grid = []
for _ in range(r):
    grid.append(list(map(int, input().split())))

ans = 0
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if grid[i][j] != s:
            continue
        top_left = grid[i - 1][j - 1]
        top_right = grid[i - 1][j + 1]
        bot_left = grid[i + 1][j - 1]
        bot_right = grid[i + 1][j + 1]
        if (top_left + top_right + bot_left + bot_right) % s == 0:
            ans += 1
print(ans)
