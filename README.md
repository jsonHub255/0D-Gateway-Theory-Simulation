# 0D Gateway Theory: Origin-Point 4D Transit

This repository contains the numerical simulation code and mathematical framework for the preprint:
**"Origin-Point 4D Transit: A Symmetrical Gateway Hypothesis"** (v2).

## Overview
The paper hypothesizes a 4D spatial coupling constrained exclusively to the 3D origin $(0,0,0)$. To avoid non-physical divergences associated with a bare 3D Dirac delta potential, the origin interaction is modeled via a self-adjoint extension defined by the Bethe-Peierls boundary condition:

$$\lim_{r \to 0} \frac{1}{\chi(r)} \frac{d\chi(r)}{dr} = -\frac{1}{a_s}$$

Where $a_s$ represents the physical s-wave scattering length capturing the 4D gateway coupling strength.

## Simulation
`simulation.py` models transmission probabilities across a potential barrier using a regularized Gaussian cutoff to represent zero-range interactions on a discrete spatial grid.

### Prerequisites
- Python 3.x
- NumPy

### Usage
```bash
python simulation.py
