import logging
import networkx as nx
from functools import lru_cache

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "11.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def count_paths_dag(graph, source, target):
    @lru_cache(maxsize=None)
    def _count(u):
        if u == target:
            return 1
        return sum(_count(v) for v in graph.successors(u))

    return _count(source)


if __name__ == "__main__":
    with open(INPUT_FILENAME) as f:
        graph = nx.parse_adjlist(
            (line.replace(":", "") for line in f), create_using=nx.DiGraph
        )

    nodes = ["svr", "fft", "dac", "out"]
    total_paths = 1
    for i in range(len(nodes) - 1):
        u, v = nodes[i], nodes[i + 1]
        count = count_paths_dag(graph, u, v)
        log.debug(f"Paths from {u} to {v}: {count}")
        total_paths *= count
    log.info(f"Final answer: {total_paths}")
