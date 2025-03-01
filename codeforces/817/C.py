from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()
    cnt = defaultdict(int)
    for word in p1:
        cnt[word] += 1
    for word in p2:
        cnt[word] += 1
    for word in p3:
        cnt[word] += 1
    score1 = 0
    score2 = 0
    score3 = 0
    for word in p1:
        if cnt[word] == 1:
            score1 += 3
        elif cnt[word] == 2:
            score1 += 1
    for word in p2:
        if cnt[word] == 1:
            score2 += 3
        elif cnt[word] == 2:
            score2 += 1
    for word in p3:
        if cnt[word] == 1:
            score3 += 3
        elif cnt[word] == 2:
            score3 += 1
    print(score1, score2, score3)
