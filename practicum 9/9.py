import os
file = 'input.txt'
kos = 0
with open('input.txt', 'r', encoding='utf-8') as sf, \
     open('output.txt', 'w', encoding='utf-8') as bh:
    for line in sf:
        kos += 1
        if kos % 2 == 0:
            bh.write(line)
