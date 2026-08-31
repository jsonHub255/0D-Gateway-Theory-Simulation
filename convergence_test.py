"""
Origin-Point 4D Transit: Numerical Convergence Test
Author: Mohammed Serraj
DOI: 10.5281/zenodo.22214878

Verifies that the Gateway Boost Factor reaches a stable asymptote as 
the grid cutoff parameter (sigma) approaches zero under Bethe-Peierls regularization.
"""

import numpy as np

def run_simulation(grid_size, sigma, a_s=-0.15, gamma=8.5):
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

sigmas = [0.15, 0.10, 0.08, 0.05, 0.03]
grid_size = 150

print("--- Convergence Test Results ---")
print(f"{'Sigma (Spatial Cutoff)':<25} | {'Gateway Boost Factor':<20}")
print("-" * 50)

for s in sigmas:
    boost = run_simulation(grid_size=grid_size, sigma=s)
    print(f"{s:<25.3f} | {boost:<20.2f}x")
