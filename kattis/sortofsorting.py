while True:
    n = int(input())
    if n == 0:
        break
    print("\n".join(sorted([input().strip() for _ in range(n)], key=lambda w: w[:2])))
