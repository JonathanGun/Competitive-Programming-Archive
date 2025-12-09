import heapq

n = int(input())
ls = list(map(int, input().split()))

print(heapq.nlargest(2, ls)[1])
