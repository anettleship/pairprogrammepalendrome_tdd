import math


def palendrome(input_int):
    while input_int > 9:
        first_digit, last_digit, updated_input = extract_first_and_last_digit(input_int)
        if first_digit != last_digit:
            return False
        input_int = updated_input
    return True 


def get_magnitude(num):
    return 10 ** int(math.log10(num))


def extract_first_and_last_digit(input_int):

    magnitude = get_magnitude(input_int)
    first_digit = input_int // magnitude
    last_digit = input_int % 10
    updated_input = (input_int - (magnitude * first_digit)) // 10

    return (first_digit, last_digit, updated_input)
