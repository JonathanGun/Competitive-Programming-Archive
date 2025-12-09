import logging

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "8.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class UnionFind:
    def __init__(self, size):
        # Initialize the parent array with each
        # element as its own representative
        self.parent = list(range(size))
        self.num_sets = size

    def find(self, i):
        # If i itself is root or representative
        if self.parent[i] == i:
            return i

        # Else recursively find the representative
        # of the parent
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        # Representative of set containing i
        irep = self.find(i)
        # Representative of set containing j
        jrep = self.find(j)
        # Make the representative of i's set
        # be the representative of j's set
        if irep != jrep:
            self.parent[irep] = jrep
            self.num_sets -= 1
            return True
        return False


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

    ans = 0
    sets = UnionFind(len(coordinates))
    for d, i, j in distances:
        log.debug(f"Distance: {d}, between points {i} and {j}")
        if sets.unite(i, j):
            if sets.num_sets == 1:
                log.info(f"Last connected node indices: {i}, {j}")
                log.info(f"Coordinates: {coordinates[i]}, {coordinates[j]}")
                ans = coordinates[i][0] * coordinates[j][0]
                break
    log.info(f"Answer: {ans}")
