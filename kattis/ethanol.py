n = int(input())

out = ['  ' for i in range(5)]
out[2] = 'H-'
for _ in range(n):
    out[0] += 'H '
    out[1] += '| '
    out[2] += 'C-'
    out[3] += '| '
    out[4] += 'H '
for i in range(5):
    if i == 2:
        out[i] += 'OH'
    else:
        out[i] += ' '

for g in out:
    print(g)
