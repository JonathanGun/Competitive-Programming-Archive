t = int(input())
for _ in range(t):
    n = int(input())
    nums = map(int, input().split())
    evens = 0
    odds = 0
    for n in nums:
        if n % 2 == 0:
            evens += n
        else:
            odds += n
    if evens > odds:
        print("YES")
    else:
        print("NO")
