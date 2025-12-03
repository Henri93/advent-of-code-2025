"""
Tests for Day 1 solution.
"""
import os
import pytest
from solution import Solution


class TestSolution:
    """Test cases for Day 1 solution."""

    @classmethod
    def get_test_file(cls, filename):
        """Get path to test file relative to this test file."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(test_dir, filename)

    def test_part1_example(self):
        """Test part 1 with example input."""
        solution = Solution()
        result = solution.part1(self.get_test_file("test_input1.txt"))
        assert result == 3
        assert isinstance(result, int)

    def test_part2_example(self):
        """Test part 2 with example input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input2.txt"))
        assert result == 6
        assert isinstance(result, int)

    def test_part1_solution(self):
        """Test part 1 with real input."""
        solution = Solution()
        result = solution.part1(self.get_test_file("input1.txt"))
        assert result == 1145
        assert isinstance(result, int)

    def test_part2_example2(self):
        """Test part 2 with real input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input2_2.txt"))
        assert result == 10
        assert isinstance(result, int)

    def test_part2_example_with_multiple_passes_and_end_on_zero(self):
        """Test part 2 with real input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input2_multiple_and_end_at_0.txt"))
        assert result == 11
        assert isinstance(result, int)

    def test_part2_example_start_on_zero(self):
        """Test part 2 with real input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input2_start_on_zero.txt"))
        assert result == 1
        assert isinstance(result, int)
    
    def test_part2_solution(self):
        """Test part 2 with real input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("input1.txt"))
        assert result == 6561
        assert isinstance(result, int)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
