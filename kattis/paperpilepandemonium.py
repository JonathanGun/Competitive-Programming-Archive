n, p = map(int, input().split())

ls = []
for _ in range(p):
    pi = list(map(int, input().split()))[1:]
    ls.append(pi)

m = int(input())
for _ in range(m):
    si, di, ni = map(int, input().split())
    ls[di - 1].extend(ls[si - 1][-ni:])
    ls[si - 1] = ls[si - 1][:-ni]

for row in ls:
    print(*row)
