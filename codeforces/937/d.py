# 11
# 121
# 1
# 14641
# 12221
# 10110
# 100000
# 99
# 112
# 2024
# 12421
# 1001

# split by 0? each group should satisfy 1, 121, 1221, 12321..?

binary_decimals = [
    10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111,
    10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111,
    11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111,
    100000
]
binary_decimals.reverse()

t = int(input())
for _ in range(t):
    n = int(input())
    for divisor in binary_decimals:
        while n % divisor == 0:
            n //= divisor
    print('YES' if n == 1 else 'NO')
