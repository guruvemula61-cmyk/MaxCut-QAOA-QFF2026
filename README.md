# Max-Cut Optimization Using QAOA

**Qiskit Fall Fest 2026 | Team Tech Titans**

## Project Overview

This project focuses on solving the Max-Cut optimization problem using the Quantum Approximate Optimization Algorithm (QAOA) with Qiskit.

The goal is to divide a weighted graph into two groups while maximizing the total weight of edges connecting the groups.

## Team Members

- Pushpa Borra
- Selsiya Gudiseva

**Institution:** Sri Vasavi Institute of Engineering and Technology, Nandamuru

## Objectives

- Formulate Max-Cut using QUBO and Ising Hamiltonians.
- Build parameterized QAOA quantum circuits.
- Optimize circuit parameters using a classical optimizer.
- Compare circuit costs across Processor A and Processor B.
- Evaluate cut quality and circuit resource requirements.
- Compare results with a classical brute-force baseline.

## Technology Stack

- Python
- Qiskit
- Qiskit Aer
- NumPy
- SciPy
- NetworkX
- Matplotlib
- Jupyter Notebook

## Workflow

1. Create a weighted graph.
2. Construct the Max-Cut cost Hamiltonian.
3. Build the QAOA circuit.
4. Optimize the QAOA parameters.
5. Transpile for the target processor architecture.
6. Measure circuit depth, gate counts, SWAPs, runtime, and cut quality.
7. Compare the results.

## Evaluation Metrics

- Best cut value
- Approximation ratio
- Optimal-cut sampling probability
- Circuit depth
- Two-qubit gate count
- SWAP count
- Execution runtime

## Future Scope

- Explore higher QAOA depths.
- Test larger graphs.
- Study noise and error mitigation.
- Extend comparisons to additional processor architectures.
- Apply the framework to other optimization problems.

## Reproducibility

The implementation, dependencies, experimental configurations, and generated results will be documented in this repository as they are added and validated.

## License

License to be decided.
