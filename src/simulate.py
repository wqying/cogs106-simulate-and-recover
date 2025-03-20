"""
This script contains the function "simulate_data" that will randomly generate
parameters alpha, nu, tau, compute predicted summary statistics, and simulate observed
statistics.
"""

import numpy as np


def simulate_data(N, alpha, nu, tau):
    """
    Simulates data based on the diffusion model.
    """
    # Random value generation
    alpha = np.random.uniform(0.5, 2)
    nu = np.random.uniform(0.5, 2)
    tau = np.random.uniform(0.1, 0.5)

    y = np.exp(-alpha * nu)
    R_pred = 1 / (y + 1)
    M_pred = tau + (alpha / (2 ** nu)) * ((1 - y) / (1 + y))
    V_pred = (alpha / (2 * (nu ** 3))) * ((1 - (2 * alpha * nu * y) - y ** 2) / (y + 1) ** 2)

    # Simulate observed values
    R_obs = np.random.binomial(N, R_pred) / N
    M_obs = np.random.normal(M_pred, np.sqrt(V_pred / N))
    V_obs = np.random.gamma((N - 1) / 2, (2 * V_pred) / (N - 1))

    return R_obs, M_obs, V_obs
