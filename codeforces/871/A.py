t = int(input())
for _ in range(t):
    # n = int(input())
    s = input()
    cf = "codeforces"
    ans = 0
    for i in range(len(s)):
        if s[i] != cf[i]:
            ans += 1
    # nums = map(int, input().split())
    print(ans)
