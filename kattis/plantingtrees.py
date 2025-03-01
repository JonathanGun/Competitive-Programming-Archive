n = int(input())
trees = sorted(map(int, input().split()), reverse=True)

mx = 0
for i, t in enumerate(trees):
    if i + t + 2 > mx:
        mx = i + t + 2
print(mx)
