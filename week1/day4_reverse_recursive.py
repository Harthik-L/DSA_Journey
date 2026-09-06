def reverse_recursive(s):
    if len(s)==0:
        return s
    return s[-1]+reverse_recursive(s[:-1])
