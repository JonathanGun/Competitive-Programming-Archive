n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    if s.startswith("+39") and 12 <= len(s) <= 13:
        cnt += 1
print(cnt)
