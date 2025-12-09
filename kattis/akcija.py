n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))
ls.sort()

total = 0
for i in range(n):
    if (n - i) % 3 == 0:
        continue
    total += ls[i]
print(total)
