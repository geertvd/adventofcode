import re
lines = open("day7/input.txt", "r").readlines()


def parse_line(line):
    parts = re.search('(.*) \((\d*)\)( \-\> (.*))?', line)
    line = {
        'name': parts.group(1),
        'weight': int(parts.group(2)),
        'parents': []
    }
    if parts.group(4):
        line['parents'] = parts.group(4).split(', ')
    else:
        line['real_weight'] = line['weight']
    return line

towers = {}
for line in lines:
    tower = parse_line(line)
    towers[tower['name']] = tower


def calc_real_weight():
    for tower_name in towers:
        tower = towers[tower_name]

        if 'real_weight' in tower.keys():
            continue

        tower_parent_weights = []
        for parent_name in tower['parents']:
            parent_tower = towers[parent_name]
            if 'real_weight' not in parent_tower.keys():
                tower_parent_weights = []
                break
            tower_parent_weights.append(parent_tower['real_weight'])

        if not tower_parent_weights:
            continue

        for index, tower_parent_weight in enumerate(tower_parent_weights):
            if tower_parent_weights.count(tower_parent_weight) == 1:
                correct_weight = tower_parent_weights[(index + 1) % len(tower_parent_weights)]
                weight_correction = correct_weight - tower_parent_weight
                print towers[tower['parents'][index]]['weight'] + weight_correction
                return True

        if not all(x == tower_parent_weights[0] for x in tower_parent_weights):
            print towers[tower['parents'][3]]
            print tower_parent_weights
            return True

        towers[tower_name]['parent_weights'] = tower_parent_weights
        towers[tower_name]['real_weight'] = sum(tower_parent_weights) + tower['weight']
    return False

found = False
while not found:
    found = calc_real_weight()
