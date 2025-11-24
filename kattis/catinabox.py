h, w, l, c = map(int, input().split())
v = h * w * l
if v == c:
    print("COZY")
elif v < c:
    print("TOO TIGHT")
else:
    print("SO MUCH SPACE")
