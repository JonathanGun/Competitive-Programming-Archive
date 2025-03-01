seq = list(map(int, list(input())))
n = int(input())
for _ in range(n):
    for i, c in enumerate(input()):
        print(chr(((ord(c) - ord('A')) * seq[i]) % 26 + ord('A')), end='')
    print()
