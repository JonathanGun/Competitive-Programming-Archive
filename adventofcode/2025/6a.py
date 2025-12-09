import logging

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "6.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == "__main__":
    inputs = []
    with open(INPUT_FILENAME, "r") as f:
        for line in f.readlines():
            inputs.append(line.strip().split())
    operators = inputs.pop()
    numbers = list(zip(*inputs))
    log.debug(f"Operators: {operators}")
    log.debug(f"Numbers: {numbers}")

    total = 0
    for i in range(len(operators)):
        op = operators[i]
        nums = list(map(int, numbers[i]))
        log.debug(f"Processing column {i} with numbers {nums} and operator {op}")
        if op == "+":
            result = 0
            for n in nums:
                result += n
        elif op == "*":
            result = 1
            for n in nums:
                result *= n
        total += result
        log.debug(f"Result for column {i} with operator {op}: {result}")
    log.info(f"Total: {total}")
