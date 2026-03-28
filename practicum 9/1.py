with open('input.txt', 'r', encoding='utf-8') as sf, \
     open('output.txt', 'w', encoding='utf-8') as bh:
    bh.writelines(line.upper() for line in sf)