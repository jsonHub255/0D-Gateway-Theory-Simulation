# Origin-Point 4D Transit: A Symmetrical Gateway Hypothesis (v3.2)

**Author:** Mohammed Serraj  
**DOI:** [10.5281/zenodo.22214878](https://doi.org/10.5281/zenodo.22214878)  
**Repository:** [jsonHub255/0D-Gateway-Theory-Simulation](https://github.com/jsonHub255/0D-Gateway-Theory-Simulation)  
**Interactive 3D Visualizer:** [jsonHub255.github.io/0D-Gateway-Theory-Simulation](https://jsonHub255.github.io/0D-Gateway-Theory-Simulation/)

---

## Overview

This repository contains the numerical simulations, mathematical derivations, and LaTeX source code for a theoretical model evaluating 4D-to-3D spatial intersections. The hypothesis evaluates quantum tunneling transmission probabilities across a 3D potential barrier featuring a localized 4D interaction constrained strictly to the origin $(0,0,0)$.

The Version 3.2 theoretical framework incorporates:
* **Bethe-Peierls Boundary Conditions:** Regularizes zero-range delta interaction terms $\psi(r) \sim C(1/r - 1/a_s)$ as $r \to 0$ to eliminate non-physical divergences.
* **Renormalization Group (RG) Scaling:** Decouples the Gaussian spatial cutoff parameter ($\sigma$) from the physical s-wave scattering length ($a_s$), proving grid-scale invariance.
* **4D-to-3D Metric Projection:** Derives the dimensional reduction of a 4D bulk metric $g_{MN}$ onto a 3D hypersurface $\Sigma_3$ using extrinsic curvature tensors.

---

## Repository Structure

```text
.
├── manuscript.tex          # Complete LaTeX source manuscript (v3.2)
├── simulation.py          # Primary WKB numerical integration script
├── convergence_test.py    # Numerical grid refinement verifier
├── plot_convergence.py    # Plotting module producing convergence_plot.png
├── convergence_plot.png   # Generated figure showing boost factor invariance
├── index.html             # Three.js interactive 3D spatial visualizer
└── README.md              # Project documentation and execution guide
