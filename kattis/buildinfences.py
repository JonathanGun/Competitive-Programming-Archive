n = int(input())
min_x, min_y, max_x, max_y = 10**8, 10**8, 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
perimeter = 2 * ((max_x - min_x + 2) + (max_y - min_y + 2))
print(perimeter)
