import logging
from typing import List

LOG_LEVEL = logging.DEBUG
INPUT_FILENAME = "5.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve(fresh_ingredients: List[List[int]], ingredients: List[int]):
    count = 0

    for ingredient in ingredients:
        for start, end in fresh_ingredients:
            if start <= ingredient <= end:
                count += 1
                log.debug(f"Ingredient {ingredient} fits in range [{start}, {end}]")
                break
    return count


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

    result = solve(fresh_ingredients, ingredients)
    log.info(f"Result: {result}")
