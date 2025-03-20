import numpy as np
import pandas as pd
from src.simulate import simulate_data
from src.recover import recover_parameters

def run_simulation(iterations=1000):
    """Runs the full simulate-and-recover experiment for N = 10, 40, 4000."""
    
    N_values = [10, 40, 4000]  # Sample sizes
    results = []  # Store results for bias and squared error

    for N in N_values:
        print(f"Running {iterations} iterations for N={N}...")

        for _ in range(iterations):
            # Step 1: Simulate Data
            alpha_true, nu_true, tau_true, R_obs, M_obs, V_obs = simulate_data(N)

            # Step 2: Recover Parameters
            recovered_params = recover_parameters(R_obs, M_obs, V_obs)

            if recovered_params is not None:
                alpha_est, nu_est, tau_est = recovered_params

                # Step 3: Compute Bias & Squared Error
                bias_alpha = alpha_true - alpha_est
                bias_nu = nu_true - nu_est
                bias_tau = tau_true - tau_est

                squared_error_alpha = bias_alpha**2
                squared_error_nu = bias_nu**2
                squared_error_tau = bias_tau**2

                # Store results
                results.append([N, bias_alpha, bias_nu, bias_tau, squared_error_alpha, squared_error_nu, squared_error_tau])

    # Convert to DataFrame and Save
    df = pd.DataFrame(results, columns=["N", "bias_alpha", "bias_nu", "bias_tau", "sq_error_alpha", "sq_error_nu", "sq_error_tau"])
    df.to_csv("results/results.csv", index=False)

    print("Simulation completed! Results saved in results/results.csv.")

if __name__ == "__main__":
    run_simulation(iterations=1000)
