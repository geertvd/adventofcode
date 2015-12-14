import re

input = file('input.txt')
time = 2503

maxdist = 0
for line in input:
    n, s, tf, tr = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds').findall(line)[0]
    curdist = 0
    curtime = 0
    fly = True
    while curtime < time:
        if fly:
            curtime += int(tf)
            curdist += int(tf) * int(s)
        else:
            curtime += int(tr)
        fly = not fly

    if not fly:
        curdist -= (curtime - time) * int(s)
    print n + ': ' + str(curdist)

    maxdist = max(maxdist, curdist)
print maxdist
