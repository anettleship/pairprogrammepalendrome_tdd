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


input_list = [11, 22, 44, 66, 88]
@pytest.mark.parametrize("list_element", input_list)
def test_palendrome_should_return_true_with_two_matching_digits(list_element):
    assert palendrome(list_element) == True


input_list = [122, 233, 455, 768, 899]
@pytest.mark.parametrize("list_element", input_list)
def test_palendroime_should_return_false_with_three_digits_first_and_last_not_matching(list_element):
    assert palendrome(list_element) == False 


input_list = [121, 232, 454, 767, 898]
@pytest.mark.parametrize("list_element", input_list)
def test_palendroime_should_return_true_with_three_digits_first_and_last_matching(list_element):
    assert palendrome(list_element) == True


input_list = [1222, 2333, 4535, 7681, 8293]
@pytest.mark.parametrize("list_element", input_list)
def test_palendroime_should_return_false_with_four_digits_first_and_last_not_matching(list_element):
    assert palendrome(list_element) == False 


input_list = [1211, 2313, 4534, 7681, 8293]
@pytest.mark.parametrize("list_element", input_list)
def test_palendroime_should_return_false_with_four_digits_middle_two_digits_not_matching(list_element):
    assert palendrome(list_element) == False 

input_list = [1111, 2332, 4554, 8888, 8228]
@pytest.mark.parametrize("list_element", input_list)
def test_palendroime_should_return_true_with_four_digits_first_and_last_matching_middle_two_matching(list_element):
    assert palendrome(list_element) == True 