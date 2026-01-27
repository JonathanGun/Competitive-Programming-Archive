n = int(input())
chosen = set()
for _ in range(n):
    _, *apps = input().split()
    for app in apps:
        if app not in chosen:
            chosen.add(app)
            print(app, end=" ")
            break
