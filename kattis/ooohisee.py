r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(input()))
# print(grid)

treasures = []
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if grid[i][j] == '0':
            found = True
            for di in range(-1, 2, 1):
                for dj in range(-1, 2, 1):
                    if di == 0 and dj == 0:
                        continue
                    if grid[i + di][j + dj] != 'O':
                        found = False    
                        break
                if not found:
                    break
            if found:
                treasures.append([i + 1, j + 1])

if not treasures:
    print("Oh no!")
elif len(treasures) > 1:
    print(f"Oh no! {len(treasures)} locations")
else:
    i, j = treasures[0]
    print(i, j)
