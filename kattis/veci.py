from itertools import permutations

x = input()
perms = sorted([int("".join(p)) for p in permutations(x)])
for p in perms:
    if p > int(x):
        print(p)
        break
else:
    print(0)
