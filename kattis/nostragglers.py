n = int(input())
total = 0
for _ in range(n):
    person, dir, x = input().split()
    x = int(x)
    if dir == "IN":
        total += x
    else:
        total -= x
if total == 0:
    print("NO STRAGGLERS")
else:
    print(total)
