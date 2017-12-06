txt = open('input.txt')

chars = 0
for line in txt:
    line = line.strip()
    chars += len(line)
    nline = eval(line)
    chars -= len(nline)


print chars
