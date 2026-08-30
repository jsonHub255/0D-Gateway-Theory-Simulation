
"""
Origin-Point 4D Transit Simulation
Author: Mohammed Serraj
DOI: 10.5281/zenodo.22140243
License: MIT License / CC BY 4.0

Description:
This numerical simulation evaluates quantum tunneling transmission probabilities 
across a baseline 3D potential barrier versus a trajectory directed through 
the exact geometric origin (0,0,0) with localized 4D spatial coupling.
"""

import numpy as np

# Spatial Grid Setup
grid_size = 100
x = np.linspace(-2, 2, grid_size)
y = np.linspace(-2, 2, grid_size)
z = np.linspace(-2, 2, grid_size)
X, Y, Z = np.meshgrid(x, y, z)

# Physical & Renormalization Parameters
# a_s: Effective s-wave scattering length induced at the origin
# sigma: Regularization width for discrete numerical grid integration
a_s = -0.15  
sigma = 0.1  
gamma = 8.5  # Integrated coupling strength over Gaussian envelope

# Baseline 3D Potential Barrier
r_sq = X**2 + Y**2 + Z**2
V_standard = 10.0 * np.exp(-r_sq)

# Regularized 4D Gateway Coupling centered at (0,0,0)
# V_reg approximates the Bethe-Peierls boundary condition on a discrete grid
gateway_coupling = gamma * (2 * np.pi * sigma**2)**(-1.5) * np.exp(-r_sq / (2 * sigma**2))

def calculate_transmission(y_off, z_off):
    x_line = np.linspace(-2, 2, grid_size)
    r_line_sq = x_line**2 + y_off**2 + z_off**2
    
    V_base = 10.0 * np.exp(-r_line_sq)
    V_delta_reg = gamma * (2 * np.pi * sigma**2)**(-1.5) * np.exp(-r_line_sq / (2 * sigma**2))
    
    # Effective Barrier path
    V_path = np.maximum(V_base - V_delta_reg, 0)
    
    dx = x_line[1] - x_line[0]
    integral = np.sum(np.sqrt(V_path)) * dx
    return np.exp(-2 * integral)

T_offcenter = calculate_transmission(0.5, 0.5)
T_origin = calculate_transmission(0.0, 0.0)

print(f"Off-Center Transmission: {T_offcenter:.6e}")
print(f"Origin (0,0,0) Transmission: {T_origin:.6e}")
print(f"Gateway Boost Factor: {T_origin / T_offcenter:.2f}x")
