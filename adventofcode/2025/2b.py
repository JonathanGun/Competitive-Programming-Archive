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
            sx = str(x)
            lx = len(sx)
            log.debug(sx)
            for i in range(lx // 2):
                if lx % (i + 1) != 0:
                    continue
                # # this is for part A
                # if i + 1 != lx / 2:
                #     continue
                pattern = sx[:i + 1]
                log.debug(f"Checking pattern length: {i + 1}, {pattern}; {sx}")
                if pattern * (lx // (i + 1)) == sx:
                    # log.info(f"Match found for {x} with pattern {pattern}")
                    cnt += 1
                    sm += x
                    break
            else:
                continue
    log.info(f"Total matches: {cnt}")
    log.info(f"Sum of matches: {sm}")
