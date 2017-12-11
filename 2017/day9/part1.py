puzzle_input = open("day9/input.txt", "r").read()

groups = []
score = 0
ignore_next_char = False
in_trash = False
for char in puzzle_input:
    if ignore_next_char:
        ignore_next_char = False
        continue

    if char == '!':
        ignore_next_char = True

    if in_trash:
        if char == '>':
            in_trash = False
        continue

    if char == '<':
        in_trash = True

    if char == '{':
        groups.append(len(groups) + 1)
    if char == '}':
        score += groups[-1]
        del groups[-1]

print score

