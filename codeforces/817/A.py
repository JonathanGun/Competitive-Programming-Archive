t = int(input())
for _ in range(t):
    n = int(input())
    s = sorted(list(input()))
    print("YES" if s == sorted(list("Timur")) else "NO")
