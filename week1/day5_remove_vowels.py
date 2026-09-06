def remove_vowels(s):
    vowels="aeiouAEIOU"
    result=""
    for char in s:
        if char not in vowels:
            result+=char
    return result
print(remove_vowels("hello world")) #hll wrld
