# test_parameterized.py
# python -m pytest test_parameterized.py

import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    ('Hello ', 'World', 'Hello World'),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
