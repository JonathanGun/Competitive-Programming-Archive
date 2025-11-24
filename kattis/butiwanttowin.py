c = int(input())
votes = sorted(map(int, input().split()))
total = sum(votes)
second = votes[-2]
others = votes[:-2]
rounds = 0

while True:
    if second * 2 > total:
        print(rounds)
        break
    if not others:
        print("IMPOSSIBLE TO WIN")
        break
    m = min(others)
    gain = 0
    new_others = []
    for v in others:
        if v == m:
            gain += v
        else:
            new_others.append(v)
    second += gain
    others = new_others
    rounds += 1
