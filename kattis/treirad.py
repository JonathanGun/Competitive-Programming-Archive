n = int(input())

cur = 1
cnt = 0
while True:
    if cur * (cur + 1) * (cur + 2) >= n:
        break
    cnt += 1
    cur += 1
print(cnt)
