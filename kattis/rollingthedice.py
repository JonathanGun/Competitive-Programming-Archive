import re
s = input()
match = re.match(r'(\d+)d(\d+)([+-]\d+)?', s)
X = int(match.group(1))
Y = int(match.group(2)) if match.group(3) else 0
Z = int(match.group(3)) if match.group(3) else 0

print((1 + Y)/2 * X + Z)
