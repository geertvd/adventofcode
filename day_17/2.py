import itertools

containers = map(int, file('input.txt').readlines())
eggnog = 150

combos = []
minimum = len(containers);
for n in range(1, len(containers) + 1):
    for combo in itertools.combinations(containers, n):
        if sum(combo) == eggnog:
            minimum = min(len(combo), minimum)
            combos.append(combo)

print len(filter(lambda x: len(x) == minimum, combos))