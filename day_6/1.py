import re
txt = open('input.txt')

regex = re.compile('([a-z ]*)(\d+),(\d+)[a-z ]*(\d+),(\d+)')

matrix = [[0 for x in range(1000)] for x in range(1000)]
for line in txt:
    state, x1, y1, x2, y2 = regex.findall(line)[0]
    state = state.strip()
    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            if state == 'turn on':
                state_value = 1
            elif state == 'turn off':
                state_value = 0
            else:
                state_value = (matrix[x][y] + 1)%2
            matrix[x][y] = state_value

print sum(x.count(1) for x in matrix)
