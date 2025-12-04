from typing import Tuple
from functools import lru_cache
import logging

LOG_LEVEL = logging.INFO
SWITCHES = 12
INPUT_FILENAME = "3.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve(digits: Tuple[int], start: int, end: int, nums: int) -> int:
    subset = digits[start:end]
    n = len(subset)
    if n < nums:
        return 0

    current_val_str = ""
    current_search_start = 0

    # greedy, pick largest digit but ensure enough digits remain
    for i in range(nums):
        search_end = n - nums + i + 1

        best_digit = -1
        best_idx = -1

        for j in range(current_search_start, search_end):
            d = subset[j]
            if d == 9:
                best_digit = 9
                best_idx = j
                break
            if d > best_digit:
                best_digit = d
                best_idx = j

        current_val_str += str(best_digit)
        current_search_start = best_idx + 1

    ans = int(current_val_str)
    log.debug(f"Answer for digits {''.join(map(str, subset))} with nums {nums}: {ans}")
    return ans


if __name__ == "__main__":
    ans = 0
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            digits = tuple([int(c) for c in line.strip()])
            cur_voltage = solve(digits, 0, len(digits), SWITCHES)
            log.debug(f"Answer for digits {line.strip()}: {cur_voltage}")
            ans += cur_voltage
    log.info(f"Final answer: {ans}")
