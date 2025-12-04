from collections import defaultdict


def is_weekday(day):
    return (day - 1) % 7 < 5


def can_schedule(orders, capacity_per_day, use_weekends):
    if not orders:
        return True

    orders = sorted(orders, key=lambda x: (x[1], x[0]))
    day_usage = defaultdict(int)
    for a, b in orders:
        scheduled = False
        for day in range(a, b + 1):
            if not use_weekends and not is_weekday(day):
                continue
            if day_usage[day] < capacity_per_day:
                day_usage[day] += 1
                scheduled = True
                break
        if not scheduled:
            return False
    return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    orders = []
    for _ in range(n):
        a, b = map(int, input().split())
        orders.append((a, b))

    capacity = m // 2

    if not can_schedule(orders, capacity, use_weekends=True):
        print("serious trouble")
    elif not can_schedule(orders, capacity, use_weekends=False):
        print("weekend work")
    else:
        print("fine")
