import logging

PAPER_ROLL_CHAR = "@"
THRESHOLD = 4
LOG_LEVEL = logging.INFO
INPUT_FILENAME = "4.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


if __name__ == "__main__":
    grid = []
    neighbors = []
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
            neighbors.append([0 for _ in range(len(line.strip()))])
    log.debug(f"Grid: {grid}")

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != PAPER_ROLL_CHAR:
                continue
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                        if grid[ni][nj] == PAPER_ROLL_CHAR:
                            neighbors[i][j] += 1

    removed = set()
    for i in range(len(neighbors)):
        for j in range(len(neighbors[i])):
            if neighbors[i][j] < THRESHOLD and grid[i][j] == PAPER_ROLL_CHAR:
                removed.add((i, j))
                log.debug(f"Initial adding [{i},{j}] to queue")

    for row in grid:
        log.debug("".join(row))
    log.info(f"Final count: {len(removed)}")
