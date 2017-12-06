import re
import itertools

distre = re.compile('(.*) to (.*) = ([\d]*)')
txt = open('input.txt')

dists = {}
points = []
for line in txt:
    line = line .strip()
    x, y, dist = distre.findall(line)[0]
    dists[x + '_' + y] = int(dist)
    if not x in points : points.append(x)
    if not y in points : points.append(y)
shortest_route_length = False
shortest_route = False
for ps in itertools.permutations(points, len(points)):
    i = 0
    length = 0
    for p in ps[0:-1]:
        length += dists[p + '_' + ps[i+1]] if p + '_' + ps[i+1] in dists else dists[ps[i+1] + '_' + p]
        i += 1

    if shortest_route == False or shortest_route_length > length:
        shortest_route = ps
        shortest_route_length = length

print shortest_route_length
print shortest_route

