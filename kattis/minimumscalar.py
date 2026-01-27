def solve() -> int:
    n = int(input())
    v1 = sorted(list(map(int, input().split())))
    v2 = sorted(list(map(int, input().split())), reverse=True)
    sm = 0
    for i in range(n):
        sm += v1[i] * v2[i]
    return sm


t = int(input())

for i in range(t):
    print(f"Case #{i + 1}: {solve()}")
