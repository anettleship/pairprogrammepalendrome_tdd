def palendrome(inputstring):
    if inputstring > 9:
        return inputstring%11 == 0
    return True