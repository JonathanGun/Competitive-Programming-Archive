from math import lcm
p, q, s = map(int, input().split())
print("yes" if lcm(p,q) >= s else "no")
