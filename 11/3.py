import string

sentence = input()

for punct in string.punctuation:
    sentence = sentence.replace(punct, ' ')

words = sentence.split()
print(words)