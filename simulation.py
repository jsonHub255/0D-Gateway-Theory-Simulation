"""
Origin-Point 4D Transit: Quantum Tunneling WKB Simulation (v3)
Author: Mohammed Serraj
DOI: 10.5281/zenodo.22214878

Calculates 1D spatial path WKB integrals across a 3D potential barrier featuring
a Bethe-Peierls regularized zero-range interaction at (0,0,0).
"""

import numpy as np

def calculate_wkb_transmission(grid_size=200, sigma=0.05, a_s=-0.15, gamma=8.5):
    x = np.linspace(-2.0, 2.0, grid_size)
    dx = x[1] - x[0]
    
    # Path passing strictly through the origin (0,0,0)
    r_sq_origin = x**2
    V_base_orig = 10.0 * np.exp(-r_sq_origin)
    V_delta_orig = gamma * (2 * np.pi * sigma**2)**(-1.5) * np.exp(-r_sq_origin / (2 * sigma**2))
    V_eff_orig = np.maximum(V_base_orig - V_delta_orig, 0)
    
    # Off-axis control path (y=0.5, z=0.5)
    r_sq_off = x**2 + 0.5**2 + 0.5**2
    V_base_off = 10.0 * np.exp(-r_sq_off)
    V_delta_off = gamma * (2 * np.pi * sigma**2)**(-1.5) * np.exp(-r_sq_off / (2 * sigma**2))
    V_eff_off = np.maximum(V_base_off - V_delta_off, 0)
    
    # WKB integrals: T ~ exp(-2 * integral(sqrt(V)))
    integral_orig = np.sum(np.sqrt(V_eff_orig)) * dx
    integral_off = np.sum(np.sqrt(V_eff_off)) * dx
    
    T_origin = np.exp(-2 * integral_orig)
    T_offaxis = np.exp(-2 * integral_off)
    boost_factor = T_origin / T_offaxis
    
    return T_origin, T_offaxis, boost_factor

if __name__ == "__main__":
    T_orig, T_off, boost = calculate_wkb_transmission()
    print("=== Origin-Point 4D Transit Simulation (v3) ===")
    print(f"Origin Transmission (T_0):       {T_orig:.6e}")
    print(f"Off-Axis Transmission (T_off):   {T_off:.6e}")
    print(f"Gateway Transmission Boost:     {boost:.2f}x")
