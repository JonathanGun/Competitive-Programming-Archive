t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    i, j = 0, n - 1
    while True:
        if i >= j:
            break
        if s[i] == s[j]:
            break
        i += 1
        j -= 1
    print(j - i + 1)
