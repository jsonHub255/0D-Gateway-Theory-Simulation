"""
Origin-Point 4D Transit: Plotting Module
Author: Mohammed Serraj
DOI: 10.5281/zenodo.22214878

Generates high-resolution visualization for the convergence of the gateway
transmission boost factor as a function of spatial cutoff parameter (sigma).
"""

import numpy as np
import matplotlib.pyplot as plt

grid_sizes = [100, 150, 200, 300]
sigmas = np.linspace(0.02, 0.20, 20)

def run_simulation(grid_size, sigma, gamma=8.5):
    x = np.linspace(-2, 2, grid_size)
    dx = x[1] - x[0]
    
    def calculate_transmission(y_off, z_off):
        r_line_sq = x**2 + y_off**2 + z_off**2
        V_base = 10.0 * np.exp(-r_line_sq)
        V_delta_reg = gamma * (2 * np.pi * sigma**2)**(-1.5) * np.exp(-r_line_sq / (2 * sigma**2))
        V_path = np.maximum(V_base - V_delta_reg, 0)
        
        integral = np.sum(np.sqrt(V_path)) * dx
        return np.exp(-2 * integral)

    T_off = calculate_transmission(0.5, 0.5)
    T_orig = calculate_transmission(0.0, 0.0)
    return T_orig / T_off

plt.figure(figsize=(8, 5))
for N in grid_sizes:
    boosts = [run_simulation(N, s) for s in sigmas]
    plt.plot(sigmas, boosts, label=f'Grid N={N}')

plt.xlabel(r'Spatial Cutoff $\sigma$', fontsize=12)
plt.ylabel('Gateway Transmission Boost Factor', fontsize=12)
plt.title('Numerical Convergence & Grid Invariance Test', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('convergence_plot.png', dpi=300)
print("Plot saved as 'convergence_plot.png'.")
