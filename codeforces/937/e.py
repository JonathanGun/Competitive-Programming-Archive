from collections import defaultdict
from math import sqrt

n = int(input())

for _ in range(n):
    x = int(input())
    s = input()
    # x is always possible
    # we can go down x//2 each step, all the way to 1 --> logX --> WRONG
    # we need to find all the factors of x, and check for each factor if it's possible --> sqrt(X)
    # we can iterate through the string, complexity = XsqrtX

    factors = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)
            if i != x // i:
                factors.append(x // i)
    factors.sort()
    factors.reverse()
    # print(x, factors)

    step = 1
    # print(s)
    last = factors[0]
    for x in factors[1:]:
        step = len(s) // x
        possible = True
        lives = 1

        # print(x, step)
        for i in range(x):
            cnts = defaultdict(int)
            for j in range(step):
                # print(i, j, x, j * x + i, s[j * x + i])
                cnts[s[j * x + i]] += 1
            # print(i, cnts)

            if len(cnts.keys()) > 2:
                possible = False
                break
            if len(cnts.keys()) == 2 and lives == 0:
                possible = False
                break
            if len(cnts.keys()) == 2:
                a, b = cnts.values()
                if min(a, b) > 1:
                    possible = False
                    break
                lives -= 1

        # print(possible, lives)
        if possible:
            last = x
    print(last)
    # print()
