t = int(input())

for _ in range(t):
    n = int(input())
    ans = [i for i in range(1, n-3+1)]
    ans.append(1 << 29)
    ans.append(1 << 30)
    last = 0
    for a in ans:
        last ^= a
    ans.append(last)
    print(*ans)
