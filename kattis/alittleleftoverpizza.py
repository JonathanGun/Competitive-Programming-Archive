import math
n = int(input())
s, m, l = 0, 0, 0
for _ in range(n):
    size, slices = input().split()
    slices = int(slices)
    if size == 'S':
        s += slices
    elif size == 'M':
        m += slices
    else:
        l += slices
print(math.ceil(s / 6) + math.ceil(m / 8) + math.ceil(l / 12))