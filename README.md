# Advent of Code 2025

Solutions for Advent of Code 2025 puzzles in Python.

## Setup

1. Create and activate the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Structure

Each day has its own directory (`day 1/` through `day 12/`) with:
- `solution.py` - Main solution code
- `input.txt` - Puzzle input (paste your input here)
- `problem.txt` - Problem description (optional)

## Running Solutions

Navigate to a day's directory and run:
```bash
cd "day 1"
python solution.py
```

Or run from the root directory:
```bash
python "day 1/solution.py"
```

## Solution Template

Day 1 uses a `Solution` class structure:
```python
class Solution:
    def __init__(self, input_file="input.txt"):
        self.data = self.read_input()

    def read_input(self):
        # Read and parse input
        pass

    def part1(self) -> int:
        # Solve part 1
        pass

    def part2(self) -> int:
        # Solve part 2
        pass
```

## Testing

Run tests and linting:
```bash
# Run all tests
pytest

# Run tests for a specific day
cd "day 1"
pytest test_solution.py -v

# Run flake8 linting
flake8 .

# Run both tests and linting
./run_tests.sh
```

### Test Structure

Each day has:
- `test_solution.py` - Unit tests with example inputs
- `test_input.txt` - Example input data with known expected outputs

Update the expected values in `test_solution.py` based on the puzzle's example inputs.
