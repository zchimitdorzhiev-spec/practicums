word = ''

with open('input.txt', 'r', encoding='utf-8') as sf, \
     open('output.txt', 'w', encoding='utf-8') as bh:
    for line in sf:
        if line:
            word += line[0]
    bh.write(word)