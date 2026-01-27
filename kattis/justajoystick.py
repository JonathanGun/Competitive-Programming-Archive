n = int(input())
name1 = input()
name2 = input()
total = 0
for i in range(n):
    c1, c2 = name1[i], name2[i]
    o1, o2 = ord(c1) - ord('A'), ord(c2) - ord('A')
    total += min(abs(o1 - o2), 26 - abs(o1 - o2))
print(total)
