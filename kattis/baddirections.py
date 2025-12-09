n = int(input())

for _ in range(n):
    k, n = input().split()
    k = int(k)
    for digit in n:
        print((int(digit) + k) % 10, end="")
    print()
