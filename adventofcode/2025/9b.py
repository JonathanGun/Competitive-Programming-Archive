import logging
import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "9.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def solve():
    coordinates = []
    try:
        with open(INPUT_FILENAME, "r") as f:
            for line in f.readlines():
                if line.strip():
                    coordinates.append(list(map(int, line.strip().split(","))))
    except FileNotFoundError:
        log.error(f"File {INPUT_FILENAME} not found")
        return

    if not coordinates:
        return

    # 1. Coordinate Compression
    xs = set()
    ys = set()
    for x, y in coordinates:
        xs.add(x)
        ys.add(y)

    # Add padding to ensure we can flood fill around the shape
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    xs.add(min_x - 1)
    xs.add(max_x + 1)
    ys.add(min_y - 1)
    ys.add(max_y + 1)

    sorted_xs = sorted(list(xs))
    sorted_ys = sorted(list(ys))

    x_map = {x: i for i, x in enumerate(sorted_xs)}
    y_map = {y: i for i, y in enumerate(sorted_ys)}

    # Grid dimensions
    # Index 2*i corresponds to sorted_xs[i]
    # Index 2*i+1 corresponds to interval (sorted_xs[i], sorted_xs[i+1])

    W = 2 * len(sorted_xs) - 1
    H = 2 * len(sorted_ys) - 1

    # 0: unknown/potential inside
    # 1: boundary
    # 2: outside
    grid = [[0] * W for _ in range(H)]

    # 2. Draw Boundary
    num_coords = len(coordinates)
    for i in range(num_coords):
        p1 = coordinates[i]
        p2 = coordinates[(i + 1) % num_coords]

        x1, y1 = p1
        x2, y2 = p2

        ix1, ix2 = x_map[x1] * 2, x_map[x2] * 2
        iy1, iy2 = y_map[y1] * 2, y_map[y2] * 2

        # Ensure ordered
        c1, c2 = min(ix1, ix2), max(ix1, ix2)
        r1, r2 = min(iy1, iy2), max(iy1, iy2)

        # Fill boundary
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] = 1

    # 3. Flood Fill Outside
    # Start from (0,0) which corresponds to (min_x-1, min_y-1)
    queue = deque([(0, 0)])
    grid[0][0] = 2

    # Directions: Up, Down, Left, Right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))

    # 4. Build Prefix Sum for Invalid Cells (Outside = 2)
    bad_grid = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 2:
                bad_grid[r][c] = 1

    # 2D Prefix Sum
    pref = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            pref[r + 1][c + 1] = (
                pref[r][c + 1] + pref[r + 1][c] - pref[r][c] + bad_grid[r][c]
            )

    def count_bad(r1, c1, r2, c2):
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

    # 5. Iterate Pairs and Check Validity
    max_area = 0

    coord_indices = []
    for x, y in coordinates:
        coord_indices.append((x_map[x] * 2, y_map[y] * 2))

    for i in range(num_coords):
        c1, r1 = coord_indices[i]
        p1 = coordinates[i]

        for j in range(i + 1, num_coords):
            c2, r2 = coord_indices[j]
            p2 = coordinates[j]

            # Define rectangle on grid
            c_min, c_max = min(c1, c2), max(c1, c2)
            r_min, r_max = min(r1, r2), max(r1, r2)

            # Check if valid (no outside cells)
            if count_bad(r_min, c_min, r_max, c_max) == 0:
                # Valid! Calculate area
                area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
                if area > max_area:
                    max_area = area
                    # log.debug(f"New max area: {max_area} from {p1} to {p2}")

    log.info(f"Final answer: {max_area}")


if __name__ == "__main__":
    solve()
