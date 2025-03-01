n, m = map(int, input().split())

ls = []
for i in range(n):
    for j, c in enumerate(input()):
        if c != '.':
            ls.append((i + j, c))
ls.sort()
print("".join(map(lambda x: x[1], ls)))
