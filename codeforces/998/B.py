def solve():
    n, m = map(int, input().split())
    ok = True
    order = [-1 for _ in range(n)]
    for i in range(n):
        ls = map(int, input().split())
        if not ok:
            continue
        ls = map(lambda x: x % n, ls)
        ls = set(ls)
        if len(ls) != 1:
            ok = False
        order[list(ls)[0]] = i + 1
    if not ok:
        print(-1)
        return
    print(" ".join(map(str, order)))

t = int(input())
for _ in range(t):
    solve()
