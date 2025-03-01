n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

is_low = False
for i in range(1, n-1):
    for j in range(1, m-1):
        cnt = 0
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if grid[i][j] < grid[ni][nj]:
                cnt += 1
        if cnt == 4:
            is_low = True
            break
    if is_low:
        break

print("Jebb" if is_low else "Neibb")
