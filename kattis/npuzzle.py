def manhattan(i, j, goal_i, goal_j):
    return abs(i - goal_i) + abs(j - goal_j)


current = []
for _ in range(4):
    current.append(input())

ans = 0
for i, row in enumerate(current):
    for j, c in enumerate(row):
        if c == ".":
            continue
        goal_i = (ord(c) - ord("A")) // 4
        goal_j = (ord(c) - ord("A")) % 4
        ans += manhattan(i, j, goal_i, goal_j)
print(ans)
