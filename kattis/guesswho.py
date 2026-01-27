n, m, q = map(int, input().split())
traits = [input().strip() for _ in range(n)]
possible = [True for _ in range(n)]

for _ in range(q):
    idx, guess = input().strip().split()
    for i, trait in enumerate(traits):
        if not possible[i]:
            continue
        if trait[int(idx) - 1] != guess:
            possible[i] = False


ans = sum(possible)
if ans == 1:
    print("unique")
    print(possible.index(True) + 1)
else:
    print("ambiguous")
    print(ans)
