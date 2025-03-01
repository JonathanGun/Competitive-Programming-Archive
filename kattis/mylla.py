def check(grid, c='O'):
    # horizontal
    for i in range(3):
        if all(map(lambda c: c == 'O', grid[i])):
            return True
    # vertical
    for j in range(3):
        for i in range(3):
            if grid[i][j] != 'O':
                break
        else:
            return True
    # diagonal
    if all(map(lambda i: grid[i][i] == 'O', range(3))):
        return True
    if all(map(lambda i: grid[i][2-i] == 'O', range(3))):
        return True
    return False


grid = [list(input()) for _ in range(3)]
won = check(grid)
print('Jebb' if won else 'Neibb')
