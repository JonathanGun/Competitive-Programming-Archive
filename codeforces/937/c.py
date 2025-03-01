n = int(input())
for _ in range(n):
    h, m = map(int, input().split(":"))
    is_am = h < 12
    h %= 12
    if h == 0:
        h = 12
    print(f"{h:02d}:{m:02d} {'AM' if is_am else 'PM'}")
