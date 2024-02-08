# test_example.py

# python -m pytest test_example.py
# A simple function to test
def add(a, b):
    return a + b

# A test function to check the add function
def test_add():
    assert add(2, 3) == 5  # Assert that 2 + 3 equals 5
    assert add('a', 'b') == 'ab'  # Testing string concatenation
