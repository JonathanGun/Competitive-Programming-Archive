words = input().split()
out = []
for word in words:
    if 'e' in word:
        out.append(word)
if out:
    print(' '.join(out))
else:
    print('oh noes')
