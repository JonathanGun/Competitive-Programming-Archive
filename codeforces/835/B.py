t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    mx = "a"
    for c in s:
        if c > mx:
            mx = c
    print(ord(mx) - ord("a") + 1)
