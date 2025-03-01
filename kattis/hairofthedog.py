n = int(input())
arr = []
for _ in range(n):
    arr.append(input() == "drunk")
# print(arr)
ans = 0
yesterday_drunk = False
for i in range(1, n - 2):
    today = arr[i]
    if today and not yesterday_drunk:
        ans += 1
        # print(i, "drunk")
        yesterday_drunk = True
    elif not today and yesterday_drunk:
        ans += 1
        # print(i, "sober")
        yesterday_drunk = True
    else:
        yesterday_drunk = False
print(ans)
