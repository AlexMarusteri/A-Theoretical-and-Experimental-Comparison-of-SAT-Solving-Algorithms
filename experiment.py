from formula import Formula
from dpll import dpll
from dp import dp
from resolution import resolution_algorithm

import time

def run_experiment(solver, clauses):
    formula = Formula(clauses)
    start = time.time()
    result = solver(formula)
    duration = time.time() - start
    return result, duration

if __name__ == "__main__":
    example = [[1, -3], [-1, 2], [-2, 3]]
    print("Running DPLL:")
    result, time_taken = run_experiment(lambda f: dpll(f)[0], example)
    print(f"Result: {result}, Time: {time_taken:.4f}s")
