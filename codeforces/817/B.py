t = int(input())
for _ in range(t):
    n = int(input())
    s = input().replace("G", "B")
    t = input().replace("G", "B")
    print("YES" if s == t else "NO")
