n, m = map(int, input().split())
monday = list(map(int, input().split()))
tuesday = list(map(int, input().split()))

for i in range(n):
    if monday[i] not in tuesday:
        print(monday[i], end=' ')
print()

for i in range(m):
    if tuesday[i] not in monday:
        print(tuesday[i], end=' ')
print()
