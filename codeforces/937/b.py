n = int(input())
for _ in range(n):
    x = int(input())
    grid = [["#" for _ in range(2*x)] for _ in range(2*x)]
    for i in range(x):
        for j in range(x):
            if (i + j) % 2 == 1:
                grid[2*i][2*j] = "."
                grid[2*i][2*j+1] = "."
                grid[2*i+1][2*j] = "."
                grid[2*i+1][2*j+1] = "."
    for g in grid:
        print("".join(g))
