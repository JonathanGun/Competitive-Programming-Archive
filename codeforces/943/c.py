t = int(input())

# print(t)

for _ in range(t):
    n = int(input())

    # print(n)

    ls = list(map(int, input().split()))
    ans = int(1e8)
    print(ans, end=" ")
    for i in range(n - 1):
        ans += ls[i]
        print(ans, end=" ")
    print()
