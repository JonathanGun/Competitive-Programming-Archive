n = int(input())

cur = 0
for _ in range(n):
    g, b = map(int, input().split())
    cur += g
    if cur < b:
        print("im", end="")
        break
print("possible")
