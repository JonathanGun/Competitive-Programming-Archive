from pprint import pprint

def mark_vis_and_detect_touch(i, j, grid, vis, n, m) -> bool:
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (not 0 <= i + di < n) or (not 0 <= j + dj < m):
                continue
            vis[i + di][j + dj] = True
            if di == 0 and dj == 0:
                continue
            if grid[i+di][j+dj] == '*':
                for di2 in range(-1, 2):
                    for dj2 in range(-1, 2):
                        ii = i + di + di2
                        jj = j + dj + dj2
                        if (not 0 <= ii < n) or (not 0 <= jj < m):
                            continue
                        vis[ii][jj] = True
                        if abs(ii - i) + abs(jj - j) <= 1:
                            continue
                        if grid[ii][jj] == '*':
                            # print(i, j, "TOUCH", ii, jj)
                            return True
    return False


def solve() -> bool:
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    potential = []
    neighbor = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                if i > 0:
                    neighbor[i-1][j] += 1
                if i < n - 1:
                    neighbor[i+1][j] += 1
                if j > 0:
                    neighbor[i][j-1] += 1
                if j < m - 1:
                    neighbor[i][j+1] += 1
    for i in range(n):
        for j in range(m):
            if neighbor[i][j] == 2 and grid[i][j] == '*':
                matches = []
                for di, dj in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    if not 0 <= i + di < n or not 0 <= j + dj < m:
                        continue
                    if grid[i + di][j + dj] == '*':
                        matches.append((di, dj))
                m1 = matches[0]
                m2 = matches[1]
                if m1[0] == m2[0] or m1[1] == m2[1]:
                    continue
                potential.append((i, j))
    # pprint(potential)
    # pprint(neighbor)
    vis = [[False] * m for i in range(n)]
    for p in potential:
        i, j = p
        touch = mark_vis_and_detect_touch(i, j, grid, vis, n, m)
        if touch:
            return False
    # print("VIS")
    # pprint(vis)
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] == '*':
                return False
    return True

t= int(input())
for _ in range(t):
    print("YES" if solve() else "NO")