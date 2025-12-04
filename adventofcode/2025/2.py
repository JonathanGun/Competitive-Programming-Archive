import logging

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "2.in"
IS_PART_TWO = False

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == "__main__":
    ranges = []
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            nums = line.split(",")
            for num in nums:
                start, end = map(int, num.split("-"))
                ranges.append((start, end))

    sm = 0
    cnt = 0
    for start, end in ranges:
        log.debug(f"Range: {start}-{end}")
        for x in range(start, end + 1):
            log.debug(x)
            # split into 2 parts
            x = str(x)
            if len(x) % 2 != 0:
                continue
            left, right = x[: len(x) // 2], x[len(x) // 2 :]
            log.debug(f"Left: {left}, Right: {right}")
            if left == right:
                cnt += 1
                sm += int(x)
                log.debug("Match found!")
    log.info(f"Total matches: {cnt}")
    log.info(f"Sum of matches: {sm}")