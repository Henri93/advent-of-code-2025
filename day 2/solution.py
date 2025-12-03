"""
Advent of Code 2025 - Day 2
"""
import os


class Solution:
    """Solution for Day 2."""

    def _resolve_path(self, filename):
        """Resolve file path relative to this script."""
        if not os.path.isabs(filename):
            return os.path.join(os.path.dirname(__file__), filename)
        return filename

    def _read_ranges(self, input_file):
        """Read and parse ranges from input file.

        Parses input where ranges are separated by commas (,) and each range
        gives its first ID and last ID separated by a dash (-).

        Returns:
            list: List of tuples (first_id, last_id) for each range
        """
        input_file = self._resolve_path(input_file)
        with open(input_file) as f:
            content = f.read().strip()
            ranges = []
            for range_str in content.split(','):
                range_str = range_str.strip()
                if range_str:
                    first_id, last_id = range_str.split('-')
                    ranges.append((int(first_id), int(last_id)))
            return ranges

    def part1(self, input_file="input1.txt") -> int:
        """
        Solve part 1 of the puzzle.

        Args:
            input_file: Path to input file

        Returns:
            int: The solution to part 1
        """
        ranges = self._read_ranges(input_file)
        invalid_ids = []
        for range_tuple in ranges:
            for num in range(range_tuple[0], range_tuple[1] + 1):
                if self._is_invalid(num):
                    invalid_ids.append(num)

        return sum(invalid_ids)
    
    def _is_invalid(self, num):
        """
        Invalid if repeats a sequence of digits twice.
        2 pointers, one at start one at mid. Traverse and check matches.
        Must be even if a sequence repeats twice! 
        """
        chars = list(str(num))
        if len(chars) % 2 != 0:
            return False
        
        start, mid = 0, len(chars) // 2
        for _ in range(start, mid):
            if chars[start] != chars[mid]:
                return False
            start += 1
            mid += 1
        
        return True

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
