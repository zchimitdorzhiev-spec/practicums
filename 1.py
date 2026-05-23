def sort_words_by_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.keys(), key=lambda w: (-word_count[w], w))
    return sorted_words

text = "яблоко банан апельсин банан яблоко банан апельсин яблоко яблоко апельсин"
result = sort_words_by_frequency(text)
print(result)
