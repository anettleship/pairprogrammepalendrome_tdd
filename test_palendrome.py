from palendrome import palendrome

def test_palendrome_should_return_true_with_single_digit_int():
    assert palendrome(1) == True

def test_palendrome_should_return_true_with_two_matching_digits():
    assert palendrome(11) == True
