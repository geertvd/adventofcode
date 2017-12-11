puzzle_input = open("day8/input.txt", "r").readlines()

local_params = {}
max_value = 0
for line in puzzle_input:
    line = line.strip()
    line_parts = line.split(' if ')
    operation = '_' + line_parts[0]
    condition = '_' + line_parts[1]

    for line_part in [operation, condition]:
        if line_part.split()[0] not in local_params.keys():
            local_params[line_part.split()[0]] = 0

    if eval(condition, {}, local_params):
        operation = operation.replace('inc', '+=')
        operation = operation.replace('dec', '-=')
        exec(operation, {}, local_params)
        if max_value < max(local_params.values()):
            max_value = max(local_params.values())

print max_value
