def char_count(s):
    counts={}
    for char in s:
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1
    return counts
print(char_count("hello")) #{'h': 1, 'e': 1, 'l': 2, 'o': 1}