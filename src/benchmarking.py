"""Benchmark QAOA solution quality against a classical reference."""

from src.maxcut import create_graph, classical_optimum
from src.qaoa import optimize_qaoa


def run_benchmark():
    graph = create_graph()

    classical_value, classical_partition = classical_optimum(graph)
    qaoa_result = optimize_qaoa(graph)

    expected_value = qaoa_result["expected_cut"]

    ratio = (
        expected_value / classical_value
        if classical_value else 0.0
    )

    results = {
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "classical_optimum": classical_value,
        "qaoa_expected_cut": round(expected_value, 6),
        "approximation_ratio": round(ratio, 6),
        "gamma": round(qaoa_result["gamma"], 6),
        "beta": round(qaoa_result["beta"], 6),
        "optimizer_iterations": qaoa_result["iterations"],
        "optimizer_success": qaoa_result["success"],
    }

    print("=== Max-Cut QAOA Benchmark ===")

    for key, value in results.items():
        print(f"{key}: {value}")

    print("Classical optimal partition:", classical_partition)

    return results


if __name__ == "__main__":
    run_benchmark()
