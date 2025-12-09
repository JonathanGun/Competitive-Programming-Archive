n = int(input())

THRESHOLD = 48
lower = False
for _ in range(n):
    length = int(input())
    if length < THRESHOLD:
        lower = True
if lower:
    print("False")
else:
    print("True")
