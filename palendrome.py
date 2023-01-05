def palendrome(input_int):
    if 10 < input_int < 100:
        return input_int%11 == 0
    elif 100 <= input_int:
        return input_int // 100 == input_int % 10
    else:
        return True