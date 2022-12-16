from palendrome import palendrome
import pytest

def test_palendrome_should_return_true_with_single_digit_int():
    assert palendrome(1) == True

def test_palendrome_should_return_true_with_two_matching_digits():
    assert palendrome(11) == True

input_list = [12, 13, 21, 31, 14]
@pytest.mark.parametrize("list_element", input_list)
def test_palendrome_should_return_false_with_two_non_matching_digits(list_element):
    assert palendrome(list_element) == False