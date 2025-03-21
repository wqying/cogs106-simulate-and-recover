"""
This script contains the function "recover_parameters" that will estimate parameters
alpha, nu, tau from simulated observed statistics and compute bias and squared error.
"""


import numpy as np


def recover_parameters(R_obs, M_obs, V_obs):
    """
    Recovers parameters from observed data using inverse EZ Diffusion equations
    """
    if R_obs in [0, 1]:
        return None

    L = np.log(R_obs / (1 - R_obs))
    numerator = L * (R_obs**2 * L - R_obs * L + R_obs - 0.5)
    denominator = V_obs

    if denominator == 0 or numerator < 0:
        return None

    nu_est = np.sign(R_obs - 0.5) * np.sqrt(np.sqrt(numerator / V_obs))

    if np.isnan(nu_est) or nu_est == 0:
        return None

    alpha_est = L / nu_est
    tau_est = M_obs - (alpha_est / (2 * nu_est)) * ((1 - np.exp(-nu_est * alpha_est)) / (1 + np.exp(-nu_est * alpha_est)))

    return alpha_est, nu_est, tau_est
