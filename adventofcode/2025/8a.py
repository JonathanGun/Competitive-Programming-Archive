import logging

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "8.in"
N = 1000
MULT_N = 3

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class UnionFind:
    def __init__(self, size):
        # Initialize the parent array with each
        # element as its own representative
        self.parent = list(range(size))

    def find(self, i):
        # If i itself is root or representative
        if self.parent[i] == i:
            return i

        # Else recursively find the representative
        # of the parent
        return self.find(self.parent[i])

    def unite(self, i, j):
        # Representative of set containing i
        irep = self.find(i)
        # Representative of set containing j
        jrep = self.find(j)
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep


if __name__ == "__main__":
    coordinates = []
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            coordinates.append(list(map(int, line.strip().split(","))))

    distances = []
    for i, (x1, y1, z1) in enumerate(coordinates):
        for j, (x2, y2, z2) in enumerate(coordinates):
            if i < j:
                if (x1, y1, z1) != (x2, y2, z2):
                    dist = abs(x1 - x2)**2 + abs(y1 - y2)**2 + abs(z1 - z2)**2
                    distances.append((dist, i, j))
                    log.debug(
                        f"Distance between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}): {dist}"
                    )
    distances.sort()

    sets = UnionFind(len(coordinates))
    for d, i, j in distances[:N]:
        log.debug(f"Distance: {d}, between points {i} and {j}")
        sets.unite(i, j)

    sizes = {}
    for i in range(len(coordinates)):
        rep = sets.find(i)
        if rep not in sizes:
            sizes[rep] = 0
        sizes[rep] += 1

    log.info(f"Number of clusters: {len(sizes)}")
    log.debug(f"Sizes: {sizes.values()}")

    ans = 1
    for size in sorted(sizes.values())[-MULT_N:]:
        ans *= size
    log.info(f"Answer: {ans}")
