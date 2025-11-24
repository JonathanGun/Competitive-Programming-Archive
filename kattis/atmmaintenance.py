n, k = map(int, input().split())
ls = list(map(int, input().split()))
res = ""
for i, x in enumerate(ls):
    if k >= x:
        res += "1"
        k -= x
    else:
        res += "0"
print(res)
