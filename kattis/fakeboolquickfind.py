class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size  # Rank helps in balancing the tree

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY

    def same_set(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)

for i in range(n):
    print(uf.find(i), end=" ")
print()
