#!/bin/bash

echo "Running all tests..."
pytest test/test_simulate.py
pytest test/test_recover.py

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Check the output above."
    exit 1
fi
