def can_reach_pile(n, m):
    if n >= m:
        return "YES" if (n - m) % 2 == 0 else "NO"
    else:
        while n < m:
            if m % 2 == 0:
                m //= 2
            else:
                m -= 1
        return "YES" if m == n else "NO"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, m = map(int, input().split())
    result = can_reach_pile(n, m)
    print(result)
