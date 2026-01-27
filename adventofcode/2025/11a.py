import logging
import networkx as nx

LOG_LEVEL = logging.INFO
INPUT_FILENAME = "11.in"

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == "__main__":
    with open(INPUT_FILENAME) as f:
        graph = nx.parse_adjlist((line.replace(":", "") for line in f), create_using=nx.DiGraph)
    log.debug(f"Graph: {graph}")

    paths = list(nx.all_simple_paths(graph, source="you", target="out"))
    log.info(f"Final answer: {len(paths)}")
