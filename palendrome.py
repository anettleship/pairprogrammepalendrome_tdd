import math


def palendrome(input_int):
    if 10 < input_int < 100:
        return input_int % 11 == 0
    elif 100 <= input_int < 1000:
        return input_int // 100 == input_int % 10
    elif input_int >= 1000:
        mid = (input_int - (1000 * (input_int // 1000))) // 10
        return (input_int // 1000 == input_int % 10) and palendrome(mid)
    else:
        return True


def get_magnitude(num):
    return 10 ** int(math.log10(num))

# Base case, input is null or <10

# Otherwise:
    # Find order of magnitude
    # Remove first and last digits
    # AND comparison of first and last digits with result of sending remaining digits to recursive call