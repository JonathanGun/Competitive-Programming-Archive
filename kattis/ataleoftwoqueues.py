n, m = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
if sum(left) > sum(right):
    print("right")
elif sum(left) < sum(right):
    print("left")
else:
    print("either")
