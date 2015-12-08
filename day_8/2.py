txt = open('input.txt')

chars = 0
for line in txt:
    line = line.strip()
    chars -= len(line)
    line = line.replace('"', '||')
    line = line.replace('\\', '||')
    line = '"' + line + '"'

    chars += len(line)


print chars
