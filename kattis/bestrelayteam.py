from heapq import nlargest

n = int(input())
first_legs = []
other_legs = []
for i in range(n):
    name, a, b = input().split()
    a = float(a)
    b = float(b)
    first_legs.append((a, i, name))
    other_legs.append((b, i, name))
other_legs.sort()

best = None
names = []
for f, i, f_name in first_legs:
    cnt = 0
    cur = f
    cur_names = []
    for other, j, name in other_legs:
        if i == j:
            continue
        if cnt >= 3:
            break
        cnt += 1
        cur += other
        cur_names.append(name)
    if best is None:
        best = cur
    if cur <= best:
        best = cur
        names = [f_name] + cur_names

print(best)
for name in names:
    print(name)
