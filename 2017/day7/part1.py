puzzle_input = open("day7/input.txt", "r").readlines()

tree = {}
for line in puzzle_input:
    line_parts = line.strip().split(' -> ')
    child = line_parts[0].split()[0]
    parents = line_parts[1].split(', ') if len(line_parts) > 1 else []

    if child not in tree.keys():
        tree[child] = 0

    tree[child] += 1

    if parents:
        for parent in parents:
            if parent not in tree.keys():
                tree[parent] = 0
            tree[parent] += 1

print min(tree, key=tree.get)
