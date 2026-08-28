
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


def run_simulation():
    # -------------------------------------------------------------------------
    # 1. Spatial Grid Configuration
    # -------------------------------------------------------------------------
    grid_size = 50
    x = np.linspace(-2.0, 2.0, grid_size)
    y = np.linspace(-2.0, 2.0, grid_size)
    z = np.linspace(-2.0, 2.0, grid_size)
    X, Y, Z = np.meshgrid(x, y, z)

    # -------------------------------------------------------------------------
    # 2. Potential Field Calculations
    # -------------------------------------------------------------------------
    # Baseline 3D Gaussian Potential Barrier
    V_standard = 10.0 * np.exp(-(X**2 + Y**2 + Z**2))

    # 4D Gateway Coupling Constant at Origin (0,0,0)
    gamma = 8.5
    r_sq = X**2 + Y**2 + Z**2
    gateway_coupling = gamma * np.exp(-r_sq / 0.01)

    # Effective Potential Barrier incorporating origin coupling
    V_gateway = np.maximum(V_standard - gateway_coupling, 0.0)

    # -------------------------------------------------------------------------
    # 3. Transmission Probability Function (WKB Approximation Model)
    # -------------------------------------------------------------------------
    def calculate_transmission(y_off, z_off):
        """Calculates transmission along a 1D path parallel to the x-axis at offset (y_off, z_off)."""
        x_line = np.linspace(-2.0, 2.0, grid_size)
        r_line_sq = x_line**2 + y_off**2 + z_off**2

        # Effective potential along trajectory
        V_path = np.maximum(
            10.0 * np.exp(-r_line_sq) - gamma * np.exp(-r_line_sq / 0.01), 0.0
        )

        dx = x_line[1] - x_line[0]
        integral = np.sum(np.sqrt(V_path)) * dx
        return np.exp(-2.0 * integral)

    # -------------------------------------------------------------------------
    # 4. Trajectory Evaluation
    # -------------------------------------------------------------------------
    T_offcenter = calculate_transmission(0.5, 0.5)
    T_origin = calculate_transmission(0.0, 0.0)
    boost_factor = T_origin / T_offcenter

    # -------------------------------------------------------------------------
    # 5. Output Results
    # -------------------------------------------------------------------------
    print("==================================================")
    print(" Origin-Point 4D Transit: Numerical Simulation ")
    print(" Author: Mohammed Serraj")
    print(" DOI: 10.5281/zenodo.22140243")
    print("==================================================")
    print(f"Off-Center Trajectory (y=0.5, z=0.5) Transmission : {T_offcenter:.6e}")
    print(f"Origin Trajectory     (y=0.0, z=0.0) Transmission : {T_origin:.6e}")
    print(f"Gateway Boost Factor                              : {boost_factor:.2f}x")
    print("==================================================")


if __name__ == "__main__":
    run_simulation()
