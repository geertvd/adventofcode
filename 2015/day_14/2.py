import re

input = file('input.txt')
time = 2503

deers = {}
maxdist = 0
for line in input:
    n, s, tf, tr = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds').findall(line)[0]
    deers[n] = {
        'mft': int(tf),
        'mrt': int(tr),
        'ft': int(tf),
        'rt': 0,
        's': int(s),
        'points': 0,
        'dist': 0
    }

for i in range(time):
    for dn in deers:
        d = deers[dn]
        if d['ft']:
            deers[dn]['dist'] += d['s']
            deers[dn]['ft'] -= 1
            deers[dn]['rt'] = d['mrt'] if not d['ft'] else 0
        else:
            deers[dn]['rt'] -= 1
            deers[dn]['ft'] = d['mft'] if not d['rt'] else 0
    maxv = max(map(lambda x: x[1]['dist'], deers.iteritems()))
    for dn in deers:
        d = deers[dn]
        if d['dist'] == maxv:
            deers[dn]['points'] += 1

for dn in deers:
    print dn + ': ' + str(deers[dn]['points'])
