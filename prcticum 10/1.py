def check():
    sentence = input()
    wovels = ['у', 'е', 'ы', 'а', 'о', 'я', 'и', 'ю']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    countW = 0
    countC = 0
    for letter in sentence.lower():
        if letter in wovels:
            countW += 1
        elif letter in consonants:
            countC += 1
    print(countC, countW)

check()