"""QAOA circuit and parameter optimization for Max-Cut."""

import numpy as np
from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

from src.maxcut import calculate_cut


def build_qaoa_circuit(graph, gamma, beta):
    """Build a single-layer QAOA circuit for a weighted graph."""
    nodes = list(graph.nodes())
    qubit = {node: index for index, node in enumerate(nodes)}
    circuit = QuantumCircuit(len(nodes))

    # Initial equal superposition
    circuit.h(range(len(nodes)))

    # Cost unitary
    for u, v, weight in graph.edges(data="weight", default=1):
        circuit.rzz(-gamma * weight, qubit[u], qubit[v])

    # Mixer unitary
    for index in range(len(nodes)):
        circuit.rx(2 * beta, index)

    return circuit


def expected_cut(graph, gamma, beta):
    """Calculate expected cut value using an exact statevector."""
    nodes = list(graph.nodes())
    circuit = build_qaoa_circuit(graph, gamma, beta)
    state = Statevector.from_instruction(circuit)
    probabilities = state.probabilities()

    expectation = 0.0

    for index, probability in enumerate(probabilities):
        bits = {
            node: (index >> position) & 1
            for position, node in enumerate(nodes)
        }
        expectation += probability * calculate_cut(graph, bits)

    return float(expectation)


def optimize_qaoa(graph, seed=42, max_iterations=200):
    """Optimize gamma and beta for a single QAOA layer."""
    rng = np.random.default_rng(seed)
    initial_parameters = rng.uniform(0, np.pi, size=2)

    result = minimize(
        fun=lambda params: -expected_cut(
            graph, params[0], params[1]
        ),
        x0=initial_parameters,
        method="COBYLA",
        options={"maxiter": max_iterations, "rhobeg": 0.5},
    )

    return {
        "gamma": float(result.x[0]),
        "beta": float(result.x[1]),
        "expected_cut": float(-result.fun),
        "success": bool(result.success),
        "iterations": int(result.nfev),
    }


if __name__ == "__main__":
    from src.maxcut import create_graph, classical_optimum

    graph = create_graph()
    classical_value, _ = classical_optimum(graph)
    result = optimize_qaoa(graph)

    print("QAOA depth: p = 1")
    print("Classical optimum:", classical_value)
    print("Optimized parameters:", result)
    print(
        "Approximation ratio:",
        result["expected_cut"] / classical_value
        if classical_value else 0.0,
    )
