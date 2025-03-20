#!/bin/bash

mkdir -p results
python3 src/main.py > results/results.csv
echo "Simulatione and results saved to results/results.csv"