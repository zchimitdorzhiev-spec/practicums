n = int(input())
dictionary = {}

for _ in range(n):
    russian, english = input().split()
    dictionary[russian] = english

phrase = input().split()
translated = []

for word in phrase:
    translated.append(dictionary.get(word, word))

print(' '.join(translated))
