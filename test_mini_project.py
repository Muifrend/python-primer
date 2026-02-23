from mini_project import calculate_binary

def test_calculate_binary_with_zero():
    assert calculate_binary(0) == "0"

def test_calculate_binary_with_positive_number():
    assert calculate_binary(5) == "101"

def test_calculate_binary_with_large_number():
    assert calculate_binary(255) == "11111111"

def test_calculate_binary_with_one():
    assert calculate_binary(1) == "1"