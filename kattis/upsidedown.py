_ = int(input())
words = sorted([word[::-1] for word in input().strip().split()], reverse=True)
print(' '.join(words))
