n, m = map(int, input().split())
ns = list(map(int, input().split()))
ms = list(map(int, input().split()))
if sum(ns) >= sum(ms):
    print("Button 1")
elif sum(ns) < sum(ms):
    print("Button 2")
else:
    print("Oh no")
