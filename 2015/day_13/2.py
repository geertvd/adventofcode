import re
import itertools
input = file('input.txt')

reg = re.compile('(.*) would (lose|gain) (\d*) happiness units by sitting next to (.*).')

people = {}
for line in input:
    p1, op, points, p2 =  reg.findall(line)[0]
    if not p1 in people:
        people[p1] = {}
    people[p1][p2] = int(points) if op == 'gain' else -int(points)

people['Geert'] = {}

allpoints = 0
for ordervariation in itertools.permutations(people.keys(), len(people)):
    ap = 0
    for i, p in enumerate(ordervariation):
        p1 = ordervariation[(i-1)%len(people)]
        p2 = ordervariation[(i+1)%len(people)]
        ap += people[p].get(p1, 0) + people[p].get(p2, 0)
    allpoints = max(allpoints, ap)

print allpoints
