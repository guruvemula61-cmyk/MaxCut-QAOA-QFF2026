import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# ==================================================
# MAX-CUT OPTIMIZATION USING QAOA
# Qiskit Fall Fest 2026 - Team Tech Titans
# ==================================================

# 1. Define a weighted graph
def create_graph():
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


G = create_graph()
N = G.number_of_nodes()
EDGES = list(G.edges(data="weight"))


# 2. Calculate the cut value
def calculate_cut(bits):
    total = 0

    for u, v, weight in EDGES:
        if bits[u] != bits[v]:
            total += weight

    return total


# 3. Find the classical optimal solution
def classical_optimum():
    best_value = -1
    best_partition = None

    for bits in itertools.product([0, 1], repeat=N):
        value = calculate_cut(bits)

        if value > best_value:
            best_value = value
            best_partition = bits

    return best_value, best_partition


# 4. Build a QAOA circuit
def build_qaoa_circuit(gamma, beta):
    circuit = QuantumCircuit(N)

    # Initial equal superposition
    circuit.h(range(N))

    # Cost unitary
    for u, v, weight in EDGES:
        circuit.rzz(-gamma * weight, u, v)

    # Mixer unitary
    for qubit in range(N):
        circuit.rx(2 * beta, qubit)

    return circuit


# 5. Calculate the expected cut value
def expected_cut(params):
    gamma, beta = params

    circuit = build_qaoa_circuit(gamma, beta)
    state = Statevector.from_instruction(circuit)
    probabilities = state.probabilities()

    expectation = 0.0

    for index, probability in enumerate(probabilities):
        bits = tuple(
            (index >> qubit) & 1
            for qubit in range(N)
        )

        expectation += probability * calculate_cut(bits)

    return expectation


# 6. Optimize QAOA parameters
def optimize_qaoa():
    initial_parameters = np.array([0.5, 0.5])

    result = minimize(
        fun=lambda params: -expected_cut(params),
        x0=initial_parameters,
        method="COBYLA",
        options={"maxiter": 200, "rhobeg": 0.5}
    )

    return result


# 7. Sample the optimized state
def sample_best_cut(params):
    gamma, beta = params

    circuit = build_qaoa_circuit(gamma, beta)
    state = Statevector.from_instruction(circuit)

    probabilities = state.probabilities()
    best_index = int(np.argmax(probabilities))

    bits = tuple(
        (best_index >> qubit) & 1
        for qubit in range(N)
    )

    return bits, probabilities[best_index]


# 8. Visualize the graph and its partition
def visualize_graph(partition):
    node_colors = [
        "teal" if partition[node] == 0 else "purple"
        for node in G.nodes()
    ]

    positions = nx.spring_layout(G, seed=42)

    edge_colors = [
        "green" if partition[u] != partition[v] else "gray"
        for u, v, weight in EDGES
    ]

    nx.draw(
        G,
        positions,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=900,
        font_weight="bold",
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G, positions, edge_labels=edge_labels
    )

    plt.title("Max-Cut Optimization Using QAOA")
    plt.tight_layout()
    plt.show()


# 9. Main execution
def main():
    print("=" * 50)
    print("MAX-CUT OPTIMIZATION USING QAOA")
    print("Qiskit Fall Fest 2026")
    print("=" * 50)

    optimal_value, optimal_partition = classical_optimum()

    print("\nClassical Benchmark")
    print("-------------------")
    print("Optimal cut value:", optimal_value)
    print("Optimal partition:", optimal_partition)

    result = optimize_qaoa()
    parameters = result.x

    qaoa_expected = expected_cut(parameters)
    approximation_ratio = qaoa_expected / optimal_value

    best_bits, best_probability = sample_best_cut(parameters)

    print("\nQAOA Results")
    print("------------")
    print("Optimized gamma:", parameters[0])
    print("Optimized beta:", parameters[1])
    print("Expected cut value:", round(qaoa_expected, 4))
    print("Approximation ratio:", round(approximation_ratio, 4))
    print("Best sampled cut:", calculate_cut(best_bits))
    print("Best-state probability:", round(float(best_probability), 4))
    print("Best sampled partition:", best_bits)

    print("\nQuantum Circuit")
    print("---------------")
    print(build_qaoa_circuit(*parameters).draw(output="text"))

    visualize_graph(best_bits)


if __name__ == "__main__":
    main()
