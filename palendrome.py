def palendrome(input_int):
    if 10 < input_int < 100:
        return input_int%11 == 0
    elif 100 <= input_int < 1000:
        return input_int // 100 == input_int % 10
    elif input_int >= 1000:
        mid = (input_int - (1000 * (input_int // 1000)))//10
        return (input_int // 1000 == input_int % 10) and palendrome(mid)
    else:
        return True