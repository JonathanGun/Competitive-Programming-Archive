n = int(input())
ls = list(map(int, input().split()))
cur = -1
ans = []
for x in ls:
    if x > cur:
        ans.append(x)
        cur = x
print(len(ans))
print(" ".join(map(str, ans)))
