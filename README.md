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

## Template

Each `solution.py` follows this structure:
- `read_input()` - Reads and parses the input file
- `part1()` - Solves part 1
- `part2()` - Solves part 2
