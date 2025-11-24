n = int(input())
print("Gnomes:")
for _ in range(n):
    ls = list(map(int, input().split()))
    sls = sorted(ls)
    if ls == sls or ls == sls[::-1]:
        print("Ordered")
    else:
        print("Unordered")
