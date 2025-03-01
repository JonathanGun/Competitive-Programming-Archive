t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    # put in 2 set, if no intersect yes, else no
    odd = set()
    for i in range(n):
        if i % 2 == 1:
            odd.add(s[i])
    even = set()
    for i in range(n):
        if i % 2 == 0:
            even.add(s[i])
    print("NO" if len(odd.intersection(even)) else "YES")
