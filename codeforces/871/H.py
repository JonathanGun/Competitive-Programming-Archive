# dp[i(2*10^5)][a(64)] = ada berapa cara bisa bikin config bit kaya gini dengan ambil elemen dari indeks-i?

# dp[i][j] = dp[i - 1][j]
# dp[i][j] += dp[i - 1][a[i] & j]
# dp[i][j] += 1

MOD = 1_000_000_007

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    dp = [[0] * 64 for i in range(n + 1)]
    # print(dp)
    for i in range(1, n + 1):
        for j in range(64):
            dp[i][j] += dp[i - 1][j]
            dp[i][j] %= MOD
            dp[i][nums[i - 1] & j] += dp[i - 1][j]
            dp[i][nums[i - 1] & j] %= MOD
        dp[i][nums[i - 1]] += 1
        dp[i][nums[i - 1]] %= MOD
    ans = 0
    for j in range(64):
        if bin(j).count("1") == k:
            ans += dp[n][j]
            ans %= MOD
    print(ans)
