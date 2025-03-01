from collections import defaultdict

n, x = map(int, input().split())
val = list(map(int, input().split()))

tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

vis = set()
q = [x]
while len(q) > 0:
    cur = q.pop(0)
    vis.add(cur)
    for child in tree[cur]:
        if child not in vis:
            val[child-1] = min(val[child-1], val[cur-1])
            q.append(child)
print(" ".join(map(str, val)))
