#!/bin/bash

echo "Starting EZ Diffusion Model simulation and recovery..."
mkdir -p results  # Ensure results directory exists

python3 src/main.py > results/results.csv

echo "Simulation completed! Results saved to results/results.csv"
