import itertools

containers = map(int, file('input.txt').readlines())
eggnog = 150

combos = []
for n in range(1, len(containers) + 1):
    for combo in itertools.combinations(containers, n):
        if sum(combo) == eggnog:
            combos.append(combo)

print len(combos)