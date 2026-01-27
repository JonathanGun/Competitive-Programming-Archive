n = int(input())
ls = list(map(int, input().split()))
for i in range(n-1):
    ls[-i-2] = min(ls[-i-1], ls[-i-2])
print(sum(ls))