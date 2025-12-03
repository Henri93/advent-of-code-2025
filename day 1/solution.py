"""
Advent of Code 2025 - Day 1
"""
import os

class Dial:
    def __init__(self):
        self.dial_pose = 50
        self.total_ticks = 100
        self.end_on_zero_count = 0
        self.times_passed_zero = 0
        print(f'The dial starts by pointing at {self.dial_pose}')

    def parseCommandAndTurn(self, command):
        dir = command[0]
        ticks_to_turn = int(command[1:])
        if dir == "L":
            self._turn_left(ticks_to_turn)
        elif dir == 'R':
            self._turn_right(ticks_to_turn)
        print(f'The dial is rotated {command} to point at {self.dial_pose}')

    def _turn_left(self, ticks):
        self._move_dial(-ticks)

    def _turn_right(self, ticks):
         self._move_dial(ticks)

    def _move_dial(self, ticks):
        start_pose = self.dial_pose
        end_position = start_pose + ticks

        times_pointed_at_zero, self.dial_pose = divmod(end_position, self.total_ticks)

        if ticks < 0:  # Left turn special handling, offset to avoid over counting at 0
            start_quotient, _ = divmod(start_pose - 1, self.total_ticks)
            end_quotient, _ = divmod(end_position - 1, self.total_ticks)
            times_pointed_at_zero = start_quotient - end_quotient

        print(f'{times_pointed_at_zero} passed 0')
        self.times_passed_zero += times_pointed_at_zero

        if self.dial_pose == 0:
            self.end_on_zero_count += 1
            print(f'ended at a 0')

class Solution:
    """Solution for Day 1."""

    def _resolve_path(self, filename):
        """Resolve file path relative to this script."""
        if not os.path.isabs(filename):
            return os.path.join(os.path.dirname(__file__), filename)
        return filename

    def _read_commands(self, input_file):
        """Read and parse commands from input file."""
        input_file = self._resolve_path(input_file)
        with open(input_file) as f:
            return [line.strip() for line in f if line.strip()]

    def part1(self, input_file="input1.txt") -> int:
        """
        Solve part 1 of the puzzle.

        Args:
            input_file: Path to input file

        Returns:
            int: The solution to part 1
        """
        commands = self._read_commands(input_file)
        dial = Dial()

        for cmd in commands:
            dial.parseCommandAndTurn(cmd)

        return dial.end_on_zero_count

    def part2(self, input_file="input2.txt") -> int:
        """
        Solve part 2 of the puzzle.

        Args:
            input_file: Path to input file

        Returns:
            int: The solution to part 2
        """
        commands = self._read_commands(input_file)
        dial = Dial()

        for cmd in commands:
            dial.parseCommandAndTurn(cmd)

        return dial.times_passed_zero


def main():
    """Main entry point."""
    solution = Solution()

    result1 = solution.part1()
    print(f"Part 1: {result1}")

    result2 = solution.part2()
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
