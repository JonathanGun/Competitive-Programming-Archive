n = int(input())
cur = 10
for _ in range(n):
    limit = input()
    if limit == "/":
        print(cur)
        continue

    print(limit)
    limit = int(limit)
    cur = max((limit + 10) // 10 * 10, cur)
