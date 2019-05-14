file = open('fem_01.txt', 'r', encoding="utf-8")
for line in file:
    print(line[line.index('='):])

file.close()