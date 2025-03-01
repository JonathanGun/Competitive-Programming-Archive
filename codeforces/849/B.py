n = int(input())
for _ in range(n):
    C = int(input())
    x, y = 0, 0
    path = input()
    for c in path:
        if c == "U":
            y -= 1
        elif c == "R":
            x += 1
        elif c == "L":
            x -= 1
        else:
            y += 1
        if x == 1 and y == -1:
            print("YES")
            break
    else:
        print("NO")
