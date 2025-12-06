"""
Advent of Code 2025 - Day 3
"""
import os
from collections import defaultdict

class Solution:
    """Solution for Day 3."""

    def _resolve_path(self, filename):
        """Resolve file path relative to this script."""
        if not os.path.isabs(filename):
            return os.path.join(os.path.dirname(__file__), filename)
        return filename

    def _read_banks(self, input_file):
        """Read and parse battery banks from input file.

        Each line represents a bank of batteries with joltage ratings (1-9).

        Returns:
            list: List of strings, each representing a bank of batteries
        """
        input_file = self._resolve_path(input_file)
        with open(input_file) as f:
            return [line.strip() for line in f if line.strip()]
        
    def _get_bank_joltage(self, bank):
        """
        Find maximum joltage by selecting two batteries in order.
        Uses digit-to-indexes mapping for efficient lookup.
        Stops as soon as we find the maximum possible combination.
        """
        digit_to_indexes = defaultdict(list)
        for i, digit in enumerate(str(bank)):
            digit_to_indexes[digit].append(i)

        # Try each digit as the first digit (in descending order)
        for first_digit in range(9, -1, -1):
            first_digit_str = str(first_digit)
            if first_digit_str not in digit_to_indexes:
                continue

            # Find the maximum second digit that appears after ANY position of first_digit
            for second_digit in range(9, -1, -1):
                second_digit_str = str(second_digit)
                if second_digit_str not in digit_to_indexes:
                    continue

                # Check if any first_digit position has this second_digit after it
                for first_pos in digit_to_indexes[first_digit_str]:
                    if any(second_pos > first_pos for second_pos in digit_to_indexes[second_digit_str]):
                        # Found the global maximum! Return immediately
                        return int(first_digit_str + second_digit_str)

        return -1

    def part1(self, input_file="input1.txt") -> int:
        """
        Solve part 1 of the puzzle.

        Find the maximum joltage possible from each bank by selecting exactly
        two batteries, then sum all maximum joltages.

        Args:
            input_file: Path to input file

        Returns:
            int: The total output joltage
        """
        banks = self._read_banks(input_file)
        bank_max_volatages = 0
        for bank in banks:
            bank_max_volatages += self._get_bank_joltage(bank)

        return bank_max_volatages

    def part2(self, input_file="input2.txt") -> int:
        """
        Solve part 2 of the puzzle.

        Args:
            input_file: Path to input file

        Returns:
            int: The solution to part 2
        """
        pass


def main():
    """Main entry point."""
    solution = Solution()

    result1 = solution.part1()
    print(f"Part 1: {result1}")

    result2 = solution.part2()
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
