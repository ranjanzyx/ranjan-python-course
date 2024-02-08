import unittest


def divide(x, y):
    """Function to divide x by y"""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


class TestAssertions(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(10, 10, "10 is not equal to 10")

    def test_assertNotEqual(self):
        self.assertNotEqual(10, 5, "10 is equal to 5")

    def test_assertTrue(self):
        self.assertTrue(10 > 5, "10 is not greater than 5")

    def test_assertFalse(self):
        self.assertFalse(10 < 5, "10 is less than 5")

    def test_assertIs(self):
        a = 'some_string'
        b = 'some_string'
        self.assertIs(a, b, "a is not b")

    def test_assertIsNone(self):
        self.assertIsNone(None, "Value is not None")

    def test_assertIn(self):
        self.assertIn(3, [1, 2, 3], "3 is not in the list")

    def test_assertRaises(self):
        with self.assertRaises(ValueError, msg="Did not raise ValueError"):
            divide(10, 0)

    def test_divide_normal_condition(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError, msg="Did not raise ValueError"):
            divide(10, 0)



unittest.main()
