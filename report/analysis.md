# Technical Analysis: Max-Cut Optimization Using QAOA

## 1. Introduction

The Max-Cut problem partitions the vertices of a graph into two sets while maximizing the total weight of edges connecting different sets.

This project explores the Quantum Approximate Optimization Algorithm (QAOA) as a method for finding high-quality solutions to Max-Cut.

## 2. Problem Formulation

Let the graph be \(G = (V,E)\), with edge weights \(w_{ij}\).

The cut objective is:

\[
C(x) = \sum_{(i,j)\in E} w_{ij}[x_i \ne x_j]
\]

where each vertex assignment \(x_i\) belongs to \(\{0,1\}\).

The objective is to maximize \(C(x)\).

## 3. Methodology

1. Construct a weighted graph.
2. Calculate a classical optimum using exhaustive enumeration.
3. Construct a parameterized QAOA quantum circuit.
4. Optimize the circuit parameters using a classical optimizer.
5. Calculate the expected cut value using a statevector simulator.
6. Compare the QAOA result against the classical optimum.

## 4. Evaluation Metrics

- **Classical optimum:** Best cut value found by exhaustive enumeration.
- **Expected cut:** Probability-weighted average cut value of the QAOA state.
- **Approximation ratio:** Expected cut divided by the classical optimum.
- **Circuit depth:** Number of sequential circuit layers after transpilation.
- **Two-qubit gate count:** Number of two-qubit operations.
- **SWAP count:** Routing operations required by a target connectivity.
- **Runtime:** Time required to execute the experiment.

## 5. Current Implementation

The initial implementation uses a small example graph and a single-layer QAOA circuit (p = 1).

The classical exhaustive search provides a reference solution. Statevector simulation evaluates the quantum circuit without sampling noise.

## 6. Processor Comparison

A valid Processor A versus Processor B comparison requires verified backend configurations, supported gates, connectivity information, and consistent transpilation settings.

The processor configuration files currently contain placeholders. Hardware comparison results should only be reported after these details are supplied and experiments are executed.

## 7. Limitations

- The current QAOA implementation uses one layer.
- The example graph is small.
- Statevector simulation does not represent real quantum hardware noise.
- Benchmark metrics must be measured from actual circuit executions.
- Demonstration website charts are not verified experimental results.

## 8. Future Work

- Implement multi-layer QAOA for p = 1, 2, and 3.
- Record optimizer convergence data.
- Add reproducible experiment outputs and CSV exports.
- Transpile circuits for verified processor architectures.
- Compare solution quality, circuit resources, and runtime.
- Update the dashboard using measured experiment results.

## 9. Conclusion

This project establishes a starting framework for evaluating QAOA on Max-Cut. Reliable conclusions about quantum processor performance require reproducible experiments and verified measurements.
