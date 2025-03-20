#!/bin/bash

echo "Starting EZ Diffusion Model simulation and recovery..."
mkdir -p results

PYTHONPATH=$(pwd) python3 src/main.py

echo "Simulation completed! Results saved to results/results.csv"
