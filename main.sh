#!/bin/bash

echo "Starting EZ Diffusion Model simulation and recovery..."
mkdir -p data output  # Ensure that these directories exist

PYTHONPATH=$(pwd) python3 src/main.py

echo "Generating plots..."
PYTHONPATH=$(pwd) python3 src/dataVisualization/visualization.py

echo "Simulation and visualization completed! Check output folder,"
