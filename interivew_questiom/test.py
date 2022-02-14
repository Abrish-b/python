def bigSentence(myStr):
    """
    this is a toptal solution for task1
    it finds the sentence with the largest
    number of words
    """
    spec = ['.', '!', '?']
    for x in spec:
        sentences = myStr.split(x)
    for y in sentences:
        print("Sentences: {}".format(str(y)))
    max = 0
    for sentence in sentences:
        words = sentence.split()
        for x in words:
            print("Words: {}".format(x))
            if max < len(words):
                max = len(words)
    return max


str1 = "We test coders. Give us a try?"
str2 = "Forget CVs..save time . x x"

print(bigSentence(str1))
print(bigSentence(str2))
print("hellow")
