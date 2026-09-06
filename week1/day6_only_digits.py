def only_digits(s):
    digits="0123456789"
    for char in s:
        if char not in digits:
            return False
    return True
print(only_digits("12345")) #True
print(only_digits("123a5")) #False