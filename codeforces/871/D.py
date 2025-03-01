from functools import lru_cache

@lru_cache(100000)
def check(n, m):
    if n < m:
        return False
    if n == m:
        return True
    if n % 3 == 0:
        return check(n // 3, m) or check(n // 3 * 2, m)
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if check(n, m) else "NO")
