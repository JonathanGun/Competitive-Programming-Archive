n, c, p = map(int, input().split())
ans = 0
for _ in range(n):
    if (x := int(input())) > c + p:
        p = c
        c = x
        ans += 1
print(ans)
