import pytest
from functions.fibonacci import generate_fibonacci

class Tests():
    def test_case1_positive(self):
        actual_result = generate_fibonacci(5)
        expected_result = [1, 1, 2, 3, 5]
        assert (actual_result == expected_result)