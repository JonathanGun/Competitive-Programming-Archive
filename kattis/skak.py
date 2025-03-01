x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
same_axes = int(x1 == x2) + int(y1 == y2)
print(abs(same_axes - 2))