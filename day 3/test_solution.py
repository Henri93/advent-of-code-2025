"""
Tests for Day 3 solution.
"""
import os
import pytest
from solution import Solution


class TestSolution:
    """Test cases for Day 3 solution."""

    @classmethod
    def get_test_file(cls, filename):
        """Get path to test file relative to this test file."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(test_dir, filename)

    def test_read_banks(self):
        """Test reading battery banks from input file."""
        solution = Solution()
        banks = solution._read_banks(self.get_test_file("test_input1.txt"))
        assert len(banks) == 4
        assert banks[0] == "987654321111111"
        assert banks[1] == "811111111111119"
        assert banks[2] == "234234234234278"
        assert banks[3] == "818181911112111"

    def test_get_bank_joltage_example1(self):
        """Test 987654321111111 -> 98 (first two batteries)."""
        solution = Solution()
        result = solution._get_bank_joltage("987654321111111")
        assert result == 98

    def test_get_bank_joltage_example2(self):
        """Test 811111111111119 -> 89 (batteries 8 and 9)."""
        solution = Solution()
        result = solution._get_bank_joltage("811111111111119")
        assert result == 89

    def test_get_bank_joltage_example3(self):
        """Test 234234234234278 -> 78 (last two batteries, 7 and 8)."""
        solution = Solution()
        result = solution._get_bank_joltage("234234234234278")
        assert result == 78

    def test_get_bank_joltage_example4(self):
        """Test 818181911112111 -> 92 (batteries 9 and 2)."""
        solution = Solution()
        result = solution._get_bank_joltage("818181911112111")
        assert result == 92
    
    def test_get_bank_joltage_example5(self):
        """Test 12345 -> 45 (batteries 4 and 5)."""
        solution = Solution()
        result = solution._get_bank_joltage("12345")
        assert result == 45

    def test_part1_example(self):
        """Test part 1 with example input.

        Expected results from problem:
        - 987654321111111 -> 98
        - 811111111111119 -> 89
        - 234234234234278 -> 78
        - 818181911112111 -> 92
        Total: 98 + 89 + 78 + 92 = 357
        """
        solution = Solution()
        result = solution.part1(self.get_test_file("test_input1.txt"))
        assert result == 357

    def test_part2_example(self):
        """Test part 2 with example input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input2.txt"))
        assert result == None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
