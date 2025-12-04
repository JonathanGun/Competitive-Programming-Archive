s = input()

t = 0
h = 0
for char in s:
    if char == "T":
        t += 1
    else:
        h += 1
    if max(t, h) >= 11 and abs(t - h) >= 2:
        t = h = 0
print(f"{t}-{h}")
