n = int(input())
mx = -1
ans = ""
for _ in range(n):
    name, v = input().split()
    v = int(v)
    if v > mx:
        mx = v
        ans = name
print(ans)
