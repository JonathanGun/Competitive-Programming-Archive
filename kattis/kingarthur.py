import math

d = float(input())
w = float(input())
n = int(input())
circumference = math.pi * d
if n * w > circumference:
    print("NO")
else:
    print("YES")
