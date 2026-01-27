import logging
from typing import List

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "9.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve(coordinates: List[List[int]]) -> int:
    max_area = 0
    n = len(coordinates)
    coordinates.sort()
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coordinates[i]
            p2 = coordinates[j]
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if area > max_area:
                max_area = area
                log.debug(f"New max area: {max_area} from points {p1} and {p2}")
    return max_area


if __name__ == "__main__":
    coordinates = []
    with open(INPUT_FILENAME, "r") as f:
        coordinates = [
            list(map(int, line.strip().split(","))) for line in f.readlines()
        ]
    log.debug(f"Coordinates: {coordinates}")
    log.info(f"Final answer: {solve(coordinates)}")
