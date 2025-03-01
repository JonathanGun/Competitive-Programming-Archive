n = int(input())
x = int(input())
ls = input().split()
pts = [0 for _ in range(n)]
for _ in range(x):
    cur = list(map(int, input().split()))
    for i in range(len(pts)):
        pts[i] += cur[i]
mx = 0
i_max = -1
for i in range(len(pts)):
    if pts[i] > mx:
        i_max = i
        mx = pts[i]
print(ls[i_max])
