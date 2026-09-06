def is_perfect_square(n):
    i=1
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False
print(is_perfect_square(16))  #True
print(is_perfect_square(15))  #False
 