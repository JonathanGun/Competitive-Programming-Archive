t = int(input())
for _ in range(t):
    n = int(input())
    min1 = 1_000_000_000
    min2 = 1_000_000_000
    both = 1_000_000_000
    for i in range(n):
        x, s = input().split()
        x = int(x)
        if s == "10":
            min1 = min(min1, x)
        elif s == "01":
            min2 = min(min2, x)
        elif s == "11":
            both = min(both, x)
    # print(min1, min2)
    ans = min(min1 + min2, both)
    if ans >= 1_000_000_000:
        print(-1)
    else:
        print(ans)
