import logging
from typing import List, Tuple
import numpy as np
from scipy.optimize import linprog

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "10.in"
ON_CHAR = "#"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve(toggles: List[List[int]], requirements: List[int]) -> int:
    m, n = len(requirements), len(toggles)
    A = np.array([[1 if i in toggle else 0 for toggle in toggles] for i in range(m)])
    result = linprog(c=np.ones(n), A_eq=A, b_eq=requirements)
    return int(round(result.fun))


def parse_line(line: str) -> Tuple[List[int], List[List[int]], List[int]]:
    parts = line.split()
    light_diagram = parts[0]
    goal = []
    for i, char in enumerate(light_diagram[1:-1]):
        if char == ON_CHAR:
            goal.append(i)

    requirements = list(map(int, parts[-1][1:-1].split(",")))

    toggles = []
    for toggle in parts[1:-1]:
        toggles.append(list(map(int, toggle[1:-1].split(","))))

    return goal, toggles, requirements


if __name__ == "__main__":
    lines = []
    with open(INPUT_FILENAME, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    total_presses = 0
    for line in lines:
        goal, toggles, requirements = parse_line(line)

        min_presses = solve(toggles, requirements)
        log.debug(f"Machine requires {min_presses} presses")
        total_presses += min_presses

    log.info(f"Final answer: {total_presses}")
