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

# Base case, input is null or <10

# Otherwise:
    # Find order of magnitude
    # Remove first and last digits
    # AND comparison of first and last digits with result of sending remaining digits to recursive call

# While loop function (input_int)
# input_int > 9  
# function extract_first_and_last_digit (returns tuple of first and last digit and new input_int with these digits removed) 
# while loop makes comparison of first and last digit
# if not a match return False
# set new input_int to result
# if reach end of loop return True

