def word_frequency(sentence):
    words=sentence.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
print(word_frequency("the cat sat on the mat")) #{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
