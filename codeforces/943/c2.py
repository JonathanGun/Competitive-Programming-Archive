t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    for i in range(n - 1):
        print(ls[i + 1] % ls[i], end=" ")
    print()
