           
#        2
#    2       2
#  2   2   2   2 
# 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0

#    4
# 0 0 0 0

# number of vertices (node) = number of edge + 1

# a + b + c (total nodes) = 2*a + b + 1
# and c != 0
# and c > a

from math import ceil

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a + b + c != 2 * a + b + 1:
        print(-1)
    elif c == 0:
        print(-1)
    elif c <= a:
        print(-1)
    else:
        h = 0
        # print("possible")
        # every node with 1 children will add 1 to the height --> wrong
        # every node with 1 children, should be spread to as many nodes C as possible, so height increase is minimal
        # height increase = ceil(B / C)
        h += ceil(b / c)
        # print(b/c, h)

        # try to pad A to the leftover slot
        slot = c
        if b > 0:
            slot -= b % c
            if slot == c:
                slot = 0
            fit = slot // 2
            # print(a, fit, slot)
            a -= fit
            slot -= fit
            slot += b % c
            if slot == 0:
                slot = c
            # print("sisa", slot, b, c)

        cur_leaves = slot
        # print(h, cur_leaves)
        # stack A to top
        # print("asd", a, cur_leaves)
        while a > 0:
            a -= cur_leaves // 2
            cur_leaves = cur_leaves // 2 + cur_leaves % 2
            # print(h, cur_leaves)
            h += 1
        print(h)
        # print()

# 8 7 9
# height: 4
#        2
#    2      2
#  2   2   2   2
# 1 1 1 1 1 1 1  2
# 0 0 0 0 0 0 0 0 0

# 3 1 4
# height: 3
#    2
#   2
# 1  2
# 0 0 0 0