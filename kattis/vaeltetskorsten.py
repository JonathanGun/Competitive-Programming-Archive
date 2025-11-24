n = int(input())
mx = 0
for _ in range(n):
    i, word = input().split()
    i = int(i)
    if word == "nej" and i > mx:
        mx = i
print(mx)
