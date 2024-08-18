import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def second_entry():
    return 2

@pytest.fixture
def order(first_entry):
    return []

@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(2)
    # Assert
    assert order == [first_entry, 2]