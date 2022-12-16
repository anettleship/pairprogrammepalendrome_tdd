def palendrome(inputstring):
    if 10 < inputstring < 100:
        return inputstring%11 == 0
    elif 100 <= inputstring:
        return inputstring // 100 == inputstring % 10
    else:
        return True