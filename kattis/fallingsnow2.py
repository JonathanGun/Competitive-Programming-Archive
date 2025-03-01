n, m = map(int, input().split())

cntSPerColumn = [0 for _ in range(m)]
for _ in range(n):
    for i, c in enumerate(list(input())):
        if c == 'S':
            cntSPerColumn[i] += 1

for i in range(n):
    for j in range(m):
        x = cntSPerColumn[j]
        if x >= n - i:
            print('S', end='')
        else:
            print('.', end='')
    print()
print()
