t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    ls = [a, b, c]
    print(sorted(ls)[1])
