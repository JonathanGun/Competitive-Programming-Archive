c = set(input())
for word in input().split():
    if len(set(word).intersection(c)) > 0:
        print('*' * len(word), end=' ')
    else:
        print(word, end=' ')
print()
