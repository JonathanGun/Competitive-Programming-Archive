grid = []
seen = []
for _ in range(8):
    grid.append(list(input().strip()))
    seen.append([False]*8)

for i in range(8):
    for j in range(8):
        if grid[i][j] == 'R':
            for ii in range(8):
                seen[ii][j] = True
            for jj in range(8):
                seen[i][jj] = True

safe_squares = 0
for i in range(8):
    for j in range(8):
        if not seen[i][j]:
            safe_squares += 1
print(safe_squares)
