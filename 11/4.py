import string

sentence = input()

for punct in string.punctuation:
    sentence = sentence.replace(punct, ' ')

words = sentence.split()
unique_words = list(dict.fromkeys(words))
print(unique_words)