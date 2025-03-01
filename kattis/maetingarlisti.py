n, r, c = map(int, input().split())

first_names = set()
for _ in range(r):
    first_names.add(input().split()[0])

for _ in range(r):
    print("left" if input() in first_names else "right")
    for _ in range(c - 1):
        input()
