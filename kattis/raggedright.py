import sys

lines = []
for line in sys.stdin:
    lines.append(len(line))
n = max(lines)

ans = 0
for m in lines[:-1]:
    ans += (n - m) ** 2
print(ans)
