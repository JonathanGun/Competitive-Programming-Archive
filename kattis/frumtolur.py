n = 100

N = 1000

is_prime = [True for _ in range(N)]
for i in range(2, N):
    p = True
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            p = False
            break
    if not p:
        for j in range(i, N, i):
            is_prime[j] = False

cnt = 0
for i, p in enumerate(is_prime):
    if cnt >= n:
        break
    if i > 1 and p:
        cnt += 1
        print(i)
