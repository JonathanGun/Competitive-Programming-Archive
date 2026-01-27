from collections import Counter

n = int(input())
cnt = Counter()
for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
    cnt[rank] = 0
for _ in range(n):
    cnt[input()[:-1]] += 1

best_bet = 4 - cnt.most_common()[-1][1]

print(best_bet / (52 - n))
