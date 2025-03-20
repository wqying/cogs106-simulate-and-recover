import csv
import matplotlib.pyplot as plt
import numpy as np


def load_results(filename):
    """
    Loads simulation results from CSV.
    """
    data = {"N": [], "bias_alpha": [], "bias_nu": [], "bias_tau": [], 
            "sq_error_alpha": [], "sq_error_nu": [], "sq_error_tau": []}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data["N"].append(int(row["N"]))
            data["bias_alpha"].append(float(row["bias_alpha"]))
            data["bias_nu"].append(float(row["bias_nu"]))
            data["bias_tau"].append(float(row["bias_tau"]))
            data["sq_error_alpha"].append(float(row["sq_error_alpha"]))
            data["sq_error_nu"].append(float(row["sq_error_nu"]))
            data["sq_error_tau"].append(float(row["sq_error_tau"]))

    return data

def plot_bias(data):
    """
    Plots bias trends for alpha, nu, and tau.
    """
    plt.figure(figsize=(8, 5))

    unique_N = sorted(set(data["N"]))
    mean_bias_alpha = [np.mean([data["bias_alpha"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]
    mean_bias_nu = [np.mean([data["bias_nu"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]
    mean_bias_tau = [np.mean([data["bias_tau"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]

    # Plot mean bias trend
    plt.plot(unique_N, mean_bias_alpha, marker='o', linestyle='-', label="Mean Bias α (Boundary Separation)")
    plt.plot(unique_N, mean_bias_nu, marker='o', linestyle='-', label="Mean Bias ν (Drift Rate)")
    plt.plot(unique_N, mean_bias_tau, marker='o', linestyle='-', label="Mean Bias τ (Non-decision Time)")

    plt.xscale("log")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)  # Expected bias = 0 line
    plt.xlabel("Sample Size (N)")
    plt.ylabel("Mean Bias")
    plt.title("Trend of Mean Bias as N Increases")
    plt.legend()
    plt.grid()
    plt.show(block=True)

    plt.savefig("bias_plot.png")

def plot_squared_error_trend(data):
    """
    Plots the mean squared error trend as N increases.
    """
    plt.figure(figsize=(8, 5))

    unique_N = sorted(set(data["N"]))
    mean_sq_error_alpha = [np.mean([data["sq_error_alpha"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]
    mean_sq_error_nu = [np.mean([data["sq_error_nu"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]
    mean_sq_error_tau = [np.mean([data["sq_error_tau"][i] for i in range(len(data["N"])) if data["N"][i] == N]) for N in unique_N]

    # Plot mean squared error trend
    plt.plot(unique_N, mean_sq_error_alpha, marker='o', linestyle='-', label="Mean Squared Error α (Boundary Separation)")
    plt.plot(unique_N, mean_sq_error_nu, marker='o', linestyle='-', label="Mean Squared Error ν (Drift Rate)")
    plt.plot(unique_N, mean_sq_error_tau, marker='o', linestyle='-', label="Mean Squared Error τ (Non-decision Time)")

    plt.xscale("log")
    plt.yscale("log")  # Squared error should decrease logarithmically
    plt.xlabel("Sample Size (N)")
    plt.ylabel("Mean Squared Error")
    plt.title("Trend of Mean Squared Error as N Increases")
    plt.legend()
    plt.grid()
    plt.show(block=True)

    plt.savefig("squared_error_plot.png")

if __name__ == "__main__":
    filename = "results.csv"
    data = load_results(filename)

    plot_bias(data)
    plot_squared_error_trend(data)
