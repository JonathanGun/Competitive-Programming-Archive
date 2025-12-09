s = int(input())
d = float(input())
t = float(input())

MPH_TO_FPS = 1.46667
if s * MPH_TO_FPS * t > d:
    print("MADE IT")
else:
    print("FAILED TEST")
