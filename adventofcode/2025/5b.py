import logging
from typing import List

LOG_LEVEL = logging.DEBUG
INPUT_FILENAME = "5.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve(fresh_ingredients: List[List[int]]):
    total = 0
    cur_start, cur_end = -1, -1
    for start, end in fresh_ingredients:
        if start > cur_end:
            if cur_start != -1:
                total += cur_end - cur_start + 1
                log.debug(f"Adding range [{cur_start}, {cur_end}] to total")
            cur_start, cur_end = start, end
        else:
            cur_end = max(cur_end, end)
    if cur_start != -1:
        total += cur_end - cur_start + 1
        log.debug(f"Adding range [{cur_start}, {cur_end}] to total")
    return total


if __name__ == "__main__":
    fresh_ingredients = []
    ingredients = []
    second_part = False
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            if not line.strip():
                second_part = True
                continue
            if not second_part:
                fresh_ingredients.append(list(map(int, line.strip().split("-"))))
            else:
                ingredients.append(int(line.strip()))
    fresh_ingredients.sort()

    result = solve(fresh_ingredients)
    log.info(f"Result: {result}")
