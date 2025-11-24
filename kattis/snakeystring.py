r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(input().strip()))

curI, curJ = -1, -1
for j in range(c):
    for i in range(r):
        if matrix[i][j] != '.':
            curI, curJ = i, j
            break
    if curI != -1:
        break

print(matrix[curI][curJ], end='')

for _ in range(c - 1):
  curJ += 1
  for deltaI in [-1, 0, 1]:
      try:
        if matrix[curI + deltaI][curJ] != '.':
            print(matrix[curI+deltaI][curJ], end='')
            curI += deltaI
            break
      except IndexError:
        pass
print()
