n, m = map(int, input().split())
seq = ['?' for x in range(n)]
valid = True
for _ in range(m):
    s, w = input().split()
    s = int(s)
    for i in range(len(w)):
        j = i + s - 1
        if seq[j] == '?' or seq[j] == w[i]:
            seq[j] = w[i]
        else:
            valid = False
            break

if not valid:
    print("Villa")
else:
    print(''.join(seq))
