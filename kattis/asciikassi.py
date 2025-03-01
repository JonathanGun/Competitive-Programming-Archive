n = int(input())
for i in range(n + 2):
    for j in range(n + 2):
        if i % (n + 1) == 0 and j % (n + 1) == 0:
            print('+', end='')
        elif i % (n + 1) == 0:
            print('-', end='')
        elif j % (n + 1) == 0:
            print('|', end='')
        else:
            print(' ', end='')
    print()
