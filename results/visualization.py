import csv
import matplotlib.pyplot as plt

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
    """Plots bias trends for alpha, nu, and tau."""
    plt.figure(figsize=(8, 5))
    plt.scatter(data["N"], data["bias_alpha"], alpha=0.5, label="Bias α (Boundary Separation)")
    plt.scatter(data["N"], data["bias_nu"], alpha=0.5, label="Bias ν (Drift Rate)")
    plt.scatter(data["N"], data["bias_tau"], alpha=0.5, label="Bias τ (Non-decision Time)")

    plt.xscale("log")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)  # Expected bias = 0 line
    plt.xlabel("Sample Size (N)")
    plt.ylabel("Bias")
    plt.title("Bias of Recovered Parameters")
    plt.legend()
    plt.grid()
    plt.show(block=True)

    plt.savefig("bias_plot.png")

def plot_squared_error(data):
    """
    Plots squared error trends for alpha, nu, and tau.
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(data["N"], data["sq_error_alpha"], alpha=0.5, label="Squared Error α (Boundary Separation)")
    plt.scatter(data["N"], data["sq_error_nu"], alpha=0.5, label="Squared Error ν (Drift Rate)")
    plt.scatter(data["N"], data["sq_error_tau"], alpha=0.5, label="Squared Error τ (Non-decision Time)")

    plt.xscale("log")
    plt.yscale("log")  # Squared error should decrease logarithmically
    plt.xlabel("Sample Size (N)")
    plt.ylabel("Squared Error")
    plt.title("Squared Error of Recovered Parameters")
    plt.legend()
    plt.grid()
    plt.show(block=True)

    plt.savefig("squared_error_plot.png")

if __name__ == "__main__":
    filename = "results.csv"
    data = load_results(filename)

    plot_bias(data)
    plot_squared_error(data)
