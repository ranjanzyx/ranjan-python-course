# test_with_fixture.py
# python -m pytest test_with_fixture.py

import pytest

# Define a fixture that sets up data before a test and cleans up after
@pytest.fixture
def sample_data():
    data = {'key': 'value'}
    # Setup before yield
    yield data
    # Teardown after yield
    data.clear()

# Use the fixture in a test by specifying its name as an argument
def test_data(sample_data):
    assert sample_data['key'] == 'value'  # Use the fixture data
