import csv
import numpy as np
from src.simulate import simulate_data
from src.recover import recover_parameters

def run_simulation(iterations=1000):
    """Runs the simulate-and-recover experiment for N = 10, 40, 4000 without using pandas."""
    
    N_values = [10, 40, 4000]  # Sample sizes
    results_file = "results/results.csv"

    # Open file for writing results
    with open(results_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["N", "bias_alpha", "bias_nu", "bias_tau", "sq_error_alpha", "sq_error_nu", "sq_error_tau"])

        for N in N_values:
            print(f"Running {iterations} iterations for N={N}...")

            for _ in range(iterations):
                # Simulate Data
                alpha_true, nu_true, tau_true, R_obs, M_obs, V_obs = simulate_data(N)

                # Recover Parameters
                recovered_params = recover_parameters(R_obs, M_obs, V_obs)

                if recovered_params is not None:
                    alpha_est, nu_est, tau_est = recovered_params

                    # Compute Bias & Squared Error
                    bias_alpha = alpha_true - alpha_est
                    bias_nu = nu_true - nu_est
                    bias_tau = tau_true - tau_est

                    squared_error_alpha = bias_alpha**2
                    squared_error_nu = bias_nu**2
                    squared_error_tau = bias_tau**2

                    # Write to CSV
                    writer.writerow([N, bias_alpha, bias_nu, bias_tau, squared_error_alpha, squared_error_nu, squared_error_tau])

    print(f"Simulation completed! Results saved in {results_file}.")

if __name__ == "__main__":
    run_simulation(iterations=1000)
