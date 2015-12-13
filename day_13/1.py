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

allpoints = 0
for ordervariation in itertools.permutations(people.keys(), len(people)):
    ap = 0
    for i, p in enumerate(ordervariation):
        p1 = ordervariation[(i-1)%len(people)]
        p2 = ordervariation[(i+1)%len(people)]
        ap += people[p][p1] + people[p][p2]
    allpoints = max(allpoints, ap)

print allpoints
