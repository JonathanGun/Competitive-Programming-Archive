n, k, d = map(int, input().split())
threshold = k + d - 14
cnt = 0
for _ in range(n):
    cnt += 1 if int(input()) >= threshold else 0
print(cnt)