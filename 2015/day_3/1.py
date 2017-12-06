from sys import argv

script, filename = argv

txt = open(filename)

directions = {
    ">": [1, 0],
    "<": [-1, 0],
    "^": [0, 1],
    "v": [0, -1]
}

x = 0
y = 0
houses = {x:{y:1}}
houses_count = 1
for char in txt.read():
    step = directions.get(char)
     x += step[0]
     y += step[1]
     if x not in houses:
         houses[x] = {}
     if y not in houses[x]:
         houses[x][y] = 1
         houses_count += 1

print houses_count

