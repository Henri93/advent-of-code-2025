"""
Tests for Day 2 solution.
"""
import os
import pytest
from solution import Solution


class TestSolution:
    """Test cases for Day 2 solution."""

    @classmethod
    def get_test_file(cls, filename):
        """Get path to test file relative to this test file."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(test_dir, filename)

    def test_is_invalid(self):
        solution = Solution()
        assert solution._is_invalid(38593859) == True
        assert solution._is_invalid(446446) == True
        assert solution._is_invalid(222222) == True
        assert solution._is_invalid(1188511885) == True
        assert solution._is_invalid(1010) == True
        assert solution._is_invalid(99) == True
        assert solution._is_invalid(11) == True
        assert solution._is_invalid(22) == True
        assert solution._is_invalid(43545) == False
        assert solution._is_invalid(10510) == False
        assert solution._is_invalid(1) == False
        assert solution._is_invalid(0) == False
        assert solution._is_invalid(222) == False

    def test_range_sum_11_22(self):
        """Test range 11-22 gives sum 11+22=33."""
        solution = Solution()
        invalid_sum = sum(num for num in range(11, 23) if solution._is_invalid(num))
        assert invalid_sum == 33

    def test_range_sum_95_115(self):
        """Test range 95-115 gives sum 99."""
        solution = Solution()
        invalid_sum = sum(num for num in range(95, 116) if solution._is_invalid(num))
        assert invalid_sum == 99

    def test_range_sum_998_1012(self):
        """Test range 998-1012 gives sum 1010."""
        solution = Solution()
        invalid_sum = sum(num for num in range(998, 1013) if solution._is_invalid(num))
        assert invalid_sum == 1010

    def test_range_sum_1188511880_1188511890(self):
        """Test range 1188511880-1188511890 gives sum 1188511885."""
        solution = Solution()
        invalid_sum = sum(num for num in range(1188511880, 1188511891) if solution._is_invalid(num))
        assert invalid_sum == 1188511885

    def test_range_sum_222220_222224(self):
        """Test range 222220-222224 gives sum 222222."""
        solution = Solution()
        invalid_sum = sum(num for num in range(222220, 222225) if solution._is_invalid(num))
        assert invalid_sum == 222222

    def test_range_sum_1698522_1698528(self):
        """Test range 1698522-1698528 gives sum 0."""
        solution = Solution()
        invalid_sum = sum(num for num in range(1698522, 1698529) if solution._is_invalid(num))
        assert invalid_sum == 0

    def test_range_sum_446443_446449(self):
        """Test range 446443-446449 gives sum 446446."""
        solution = Solution()
        invalid_sum = sum(num for num in range(446443, 446450) if solution._is_invalid(num))
        assert invalid_sum == 446446

    def test_range_sum_38593856_38593862(self):
        """Test range 38593856-38593862 gives sum 38593859."""
        solution = Solution()
        invalid_sum = sum(num for num in range(38593856, 38593863) if solution._is_invalid(num))
        assert invalid_sum == 38593859

    def test_part1_example(self):
        """Test part 1 with example input."""
        solution = Solution()
        result = solution.part1(self.get_test_file("test_input1.txt"))
        assert result == 1227775554

    def test_part1(self):
        """Test part 1 with real input."""
        solution = Solution()
        result = solution.part1(self.get_test_file("input1.txt"))
        assert result == 40214376723

    def test_part2_example(self):
        """Test part 2 with example input."""
        solution = Solution()
        result = solution.part2(self.get_test_file("test_input1.txt"))
        assert result == 4174379265

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
