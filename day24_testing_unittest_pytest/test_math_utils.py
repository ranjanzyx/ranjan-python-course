import unittest
from math_utils import add, subtract

class MyMathTest(unittest.TestCase):

    def test_add_positive(self):
        """Tests the addition of positive numbers."""
        result = add(2, 3)
        self.assertEqual(result, 50, "Adding 2 and 3 should return 5")

    def test_add_negative(self):
        """Tests the addition of negative numbers."""
        result = add(-2, 1)
        self.assertEqual(result, -1, "Adding -2 and 1 should return -1")

    def test_subtract_positive(self):
        """Tests the subtraction of positive numbers."""
        result = subtract(8, 4)
        self.assertEqual(result, 4, "Subtracting 4 from 8 should return 4")

    def test_subtract_negative(self):
        """Tests the subtraction of negative numbers."""
        result = subtract(-2, 1)
        self.assertEqual(result, -3, "Subtracting 1 from -2 should return -3")

if __name__ == "__main__":
    unittest.main()
