import re
import itertools

distre = re.compile('(.*) to (.*) = ([\d]*)')
txt = open('input.txt')

dists = {}
points = []
for line in txt:
    line = line .strip()
    x, y, dist = distre.findall(line)[0]
    dists[x + '_' + y] = dists[y + '_' + x] = int(dist)
    if not x in points : points.append(x)
    if not y in points : points.append(y)
longest_route_length = False
longest_route = False
for ps in itertools.permutations(points, len(points)):
    i = 0
    length = 0
    for p in ps[0:-1]:
        length += dists[p + '_' + ps[i+1]]
        i += 1

    if longest_route == False or longest_route_length < length:
        longest_route = ps
        longest_route_length = length

print longest_route_length
print longest_route

