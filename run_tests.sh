#!/bin/bash
# Run tests and linting for Advent of Code solutions

set -e

echo "=== Running flake8 linting ==="
flake8 .

echo ""
echo "=== Running pytest ==="
pytest

echo ""
echo "=== All checks passed! ==="
