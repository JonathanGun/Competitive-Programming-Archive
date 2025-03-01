# traverse to all node from A, log XOR of path for every node -> store in set
# do the same from B
# if intersection set A and B not empty, print YES

def dfs(cur, parent, x):
    if cur == b:
        return
    pathA.add(x)
    for neigh, w in tree[cur]:
        if neigh == parent:
            continue
        dfs(neigh, cur, x^w)

def dfsB(cur, parent, x):
    if cur != b and x in pathA:
        return True
    for neigh, w in tree[cur]:
        if neigh == parent:
            continue
        if dfsB(neigh, cur, x ^ w):
            return True
    return False

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    tree = [[] for i in range(n + 1)]
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        tree[u].append((v, w))
        tree[v].append((u, w))

    pathA = set()
    dfs(a, -1, 0)
    if dfsB(b, -1, 0):
        print("YES")
    else:
        print("NO")
