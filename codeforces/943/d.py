t = int(input())

for _ in range(t):
    n, k, posB, posS = map(int, input().split())
    perms = list(map(int, input().split()))
    score = list(map(int, input().split()))

    ans = map(lambda x: n * x, score)
    for i in range(n):
        for j in range(n):
            ans = max(ans, (n - i) * score[j])