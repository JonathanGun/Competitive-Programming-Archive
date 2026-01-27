import logging
from typing import List, Tuple
from collections import deque

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "10.test"
ON_CHAR = "#"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def mask_to_int(mask: List[int]) -> int:
    result = 0
    for bit in mask:
        result += 1 << bit
    return result


def solve(toggles: List[List[int]], goal: int) -> int:
    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        current, presses = queue.popleft()
        if current == goal:
            return presses
        for toggle in toggles:
            toggle_mask = mask_to_int(toggle)
            new_current = current ^ toggle_mask
            if new_current not in visited:
                visited.add(new_current)
                queue.append((new_current, presses + 1))
    return -1


def parse_line(line: str) -> Tuple[str, List[List[int]], List[int]]:
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
    log.debug(f"Lines: {lines}")

    total_presses = 0
    for line in lines:
        # input parsing
        goal, toggles, requirements = parse_line(line)
        goal_as_int = mask_to_int(goal)
        log.debug(
            f"Goal positions: {goal}, as int: {goal_as_int}, toggles: {toggles}, requirements: {requirements}"
        )

        # solve
        min_presses = solve(toggles, goal_as_int)
        log.debug(f"Machine with goal {goal} requires {min_presses} presses")
        total_presses += min_presses

    log.info(f"Final answer: {total_presses}")
