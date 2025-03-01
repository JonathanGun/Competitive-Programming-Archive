def solve():
    x = int(input())
    ls = list(map(int, input().split()))
    for i in range(1, x):
        y = min(ls[i], ls[i - 1])
        ls[i] -= y
        ls[i - 1] -= y
    return ls == sorted(ls)

n = int(input())
for _ in range(n):
    ans = solve()
    if ans:
        print("YES")
    else:
        print("NO")
