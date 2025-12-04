import logging

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "3.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

# take largest digit from index 1 to N
# take largest digit from index i+1 to N (where i is the index taken previously)
# if i == N-1, take second largest from index 0 to N-1

def solve(line: str) -> int:
    log.debug(f"Solving for line: {line}")
    ans = 0
    digits = [int(c) for c in line]
    mx = max(digits)
    i = digits.index(mx)
    if i == len(digits) - 1:
        ans += mx
        log.debug(f"Second digit: {mx}")
        digits.remove(mx)
        mx = max(digits)
        log.debug(f"First digit: {mx}")
        ans += mx * 10
    else:
        ans += mx * 10
        mx2 = max(digits[i + 1 :])
        ans += mx2
    log.debug(f"Answer for line: {ans}")
    return ans

if __name__ == "__main__":
    ans = 0
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            ans += solve(line.strip())
    log.info(f"Final answer: {ans}")
