#!/bin/bash

echo "Running all tests..."

# Run tests explicitly by path
python3 -m unittest discover -s test -p "*.py"

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Check the output above."
    exit 1
fi
