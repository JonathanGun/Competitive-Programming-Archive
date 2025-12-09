import logging
from typing import List

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "7.in"
SPLITTER_CHAR = "^"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


if __name__ == "__main__":
    grid: List[List[int]] = []
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            grid.append(line.strip())

    cnt = 0
    beams = set([grid[0].index("S")])
    for i in range(1, len(grid)):
        for j in beams.copy():
            if grid[i][j] == SPLITTER_CHAR:
                beams.add(j - 1)
                beams.add(j + 1)
                beams.remove(j)
                log.debug(f"Beam at row {i}, col {j} split into {j-1} and {j+1}")
                cnt += 1
    log.info(f"Total splits: {cnt}")
