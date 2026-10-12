"""Max-Cut graph creation and classical reference solver."""

import itertools
import networkx as nx


def create_graph():
    """Create the project's example weighted graph."""
    graph = nx.Graph()

    graph.add_weighted_edges_from([
        (0, 1, 1),
        (0, 2, 1),
        (1, 2, 1),
        (1, 3, 1),
        (2, 3, 1),
        (3, 4, 1),
    ])

    return graph


def calculate_cut(graph, bits):
    """Return the total weight of edges crossing two partitions."""
    return sum(
        weight
        for u, v, weight in graph.edges(data="weight", default=1)
        if bits[u] != bits[v]
    )


def classical_optimum(graph):
    """Find an exact Max-Cut solution by exhaustive enumeration."""
    nodes = list(graph.nodes())
    best_value = -1
    best_partition = None

    for bits in itertools.product([0, 1], repeat=len(nodes)):
        partition = dict(zip(nodes, bits))
        value = calculate_cut(graph, partition)

        if value > best_value:
            best_value = value
            best_partition = partition

    return best_value, best_partition


if __name__ == "__main__":
    graph = create_graph()
    value, partition = classical_optimum(graph)

    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    print("Classical optimal cut:", value)
    print("Partition:", partition)
