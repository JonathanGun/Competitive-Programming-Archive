MOD = 998_244_353


def count(factors, total_nums):
    if not factors:
        return total_nums
    print(factors, total_nums)
    nums = list(map(lambda x: x[1], factors))
    n = sum(nums)
    nums.append(total_nums - n)
    x = max(nums)
    print(n, "C", x)
    ans = 1
    print("ans", ans)
    for i in range(total_nums, total_nums - x, -1):
        print(i)
        ans *= i
        ans %= MOD
    print("atas", ans, "/", nums)
    for num in nums:
        ans //= num
    return ans


def factorize(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors.append((i, cnt))
    return factors


def solve():
    k, n = map(int, input().split())
    for i in range(1, k + 1):
        factors = factorize(i)
        x = count(factors, n)
        # print(x, end=" ")
        print(i, factors, n, "ans:", x)
        print()
    print()


n = int(input())
for _ in range(n):
    solve()

# print(factorize(2**5 * 3**3 * 5**2))
