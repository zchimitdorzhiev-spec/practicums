try:
    with open('input.txt', 'r', encoding='utf-8') as sf, \
         open('output.txt', 'w', encoding='utf-8') as bh:
        num = sf.readline()
        count = len(sf.readlines())

        if int(num) == count:
            bh.write('YES')
        else:
            bh.write('NO')
except ValueError:
    with open('input.txt', 'r', encoding='utf-8') as sf, \
         open('output.txt', 'w', encoding='utf-8') as bh:
        bh.write('Error')