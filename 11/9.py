import string

text = ""
while True:
    line = input()
    if line == "":
        break
    text += " " + line

for punct in string.punctuation:
    text = text.replace(punct, " ")

words = text.lower().split()

freq = {}
order = []

for w in words:
    if w not in freq:
        freq[w] = 0
        order.append(w)
    freq[w] += 1

result = sorted(order, key=lambda w: freq[w], reverse=True)

for w in result:
    print(w)