n = int(input())
locations = [input().strip() for _ in range(n)]
start = locations[0]
sm = 0
for loc in locations[1:]:
    cur_a, cur_b = loc[0], loc[1]
    start_a, start_b = start[0], start[1]
    sm += abs(ord(start_a) - ord(cur_a)) + abs(ord(start_b) - ord(cur_b))
    start = loc
print(sm)
