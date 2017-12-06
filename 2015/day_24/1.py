import itertools


presents = map(int, file('input.txt').readlines())
group_weight = sum(presents) / 3

good_combos = []
for r in xrange(2, (len(presents) / 3) + 1):
    for combo in itertools.combinations(presents, r):
        if sum(combo) == group_weight:
            good_combos.append(combo)

good_combos.sort(key = len)
smallest_group = 10
smallest_qe = 100000000000
for combo_1 in good_combos:
    if len(combo_1) > smallest_group:
        break
    for good_combo_2 in good_combos:
        if len(set(combo_1) & set(good_combo_2)) == 0:
            smallest_group = len(combo_1)
            smallest_qe = min(smallest_qe, reduce(lambda x, y: x*y, combo_1))

print smallest_group
print smallest_qe
