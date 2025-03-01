N = 200_005
arr = [0 for i in range(N)]
diff = [0 for i in range(N)]


def lowbit(x):
    return x & (-x)


def add(x, v, n):
    i = x
    while i <= n:
        diff[i] += v
        i += lowbit(i)


def askSum(x):
    ans = 0
    i = x
    while i >= 1:
        ans += diff[i]
        i -= lowbit(i)
    return ans
