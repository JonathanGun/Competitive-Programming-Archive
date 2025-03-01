a, b = map(int, input().split())
x = min(a, b)
ans = x * 10
a -= x
ans += (a // 3) * 10
a %= 3
ans += (a // 2) * 3
a %= 2
ans += a
print(ans)
