r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(input()))

vis = [[False for _ in range(c)] for _ in range(r)]

cnt = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == '#' and not vis[i][j]:
            # print(i, j)
            start = (i, j)
            prev = None
            cur = start
            while True:
                found = False
                vis[cur[0]][cur[1]] = True
                neighbors = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1)
                ]
                for di, dj in neighbors:
                    ii = cur[0] + di
                    jj = cur[1] + dj
                    if ii < 0 or ii >= r or jj < 0 or jj >= c:
                        continue
                    if ((ii, jj) == start and prev != start) or (grid[ii][jj] == '#' and not vis[ii][jj]):
                        prev = cur
                        cur = (ii, jj)
                        found = True
                        # print("found", cur)
                        break
                if cur == start:
                    # print(cur, cnt)
                    cnt += 1
                    break

print(cnt)
