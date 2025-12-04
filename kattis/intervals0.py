n, k = map(int, input().split())
events = []
for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))
    events.append((b, -1))
events.sort()

count = 0
current_users = 0
prev_time = 0

for time, delta in events:
    if current_users >= k:
        count += time - prev_time
    current_users += delta
    prev_time = time

print(count)
