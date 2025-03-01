name = input()
n = int(input())
for j in range(n):
    cnt = 0
    check = input()
    for i, c in enumerate(name):
        if c != check[i]:
            cnt += 1
    if cnt == 1:
        print(j + 1)
        break
else:
    print(n)
