# SAT Solving Algorithms

This repository contains the source code implementations of the SAT (Boolean Satisfiability Problem) solving algorithms discussed in the scientific paper:

**"A Theoretical and Experimental Comparison of SAT Solving Algorithms"**

## Overview

The purpose of this repository is to provide reference implementations of various SAT solvers analyzed in the paper. These implementations are designed to:

- Enable reproducibility of the experimental results.
- Support comparative analysis of theoretical and practical performance.
- Serve as educational and research tools for understanding SAT solving strategies.

## Paper Reference

If you use this code in your research or project, please cite the paper:

**A Theoretical and Experimental Comparison of SAT Solving Algorithms**  
*Author(s): [Your Name(s)]*  
*Year: [Year of Publication]*  
*DOI/Link: [Insert Link or DOI if available]*

## Contents

- `dpll/` – Implementation of the DPLL algorithm and its variants.
- `cdcl/` – Conflict-Driven Clause Learning based solvers.
- `walksat/` – Stochastic local search solvers like WalkSAT.
- `benchmarks/` – Benchmark instances used in the experiments.
- `scripts/` – Scripts for running experiments and analyzing results.

## Requirements

This project uses Python (or C++, etc. adjust based on your implementation language). To set up the environment:

```bash
# Example for Python
pip install -r requirements.txt
