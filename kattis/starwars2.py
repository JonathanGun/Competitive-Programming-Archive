n = int(input())
ls = sorted(map(int, input().split()))

for i in range(n // 3, 2 * n // 3):
    print(ls[i], end=" ")
for i in range(n // 3):
    print(ls[i], end=" ")
for i in range(2 * n // 3, n):
    print(ls[i], end=" ")
print()