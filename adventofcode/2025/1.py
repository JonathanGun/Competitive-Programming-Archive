from typing import Tuple
import logging

LOG_LEVEL = logging.INFO
DIAL_SIZE = 100
DIAL_START = 50
INPUT_FILENAME = "1.in"
IS_PART_TWO = True

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


# move the dial and return new position and number of clicks
def move(cur: int, direction: str, distance: int) -> Tuple[int, int]:
    total_dist = distance
    if direction == "L":
        total_dist += (DIAL_SIZE - cur) % DIAL_SIZE
        cur -= distance
    elif direction == "R":
        total_dist += cur
        cur += distance
    log.debug(f"Total distance adjusted: {total_dist}")

    clicks = total_dist // DIAL_SIZE
    cur %= DIAL_SIZE
    if not IS_PART_TWO:
        if cur == 0:
            clicks += 1
    log.debug(f"Clicks this move: {clicks}")
    return cur, clicks


if __name__ == "__main__":
    cur = DIAL_START
    cnt = 0
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            direction, distance = line[0], line[1:].strip()
            distance = int(distance)
            log.debug(f"Current: {cur}, Direction: {direction}, Distance: {distance}")
            cur, clicks = move(cur, direction, distance)
            if clicks:
                cnt += clicks
    log.info(f"Total clicks: {cnt}")
