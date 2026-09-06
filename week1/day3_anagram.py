def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count1={}
    count2={}
    for char in s1:
        count1[char]=count1.get(char,0)+1
    for char in s2:
        count2[char]=count2.get(char,0)+1
    return count1==count2
print(is_anagram("listen","silent"))   #True
print(is_anagram("hello","world"))  #False