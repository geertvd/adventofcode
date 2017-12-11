puzzle_input = open("day8/input.txt", "r").readlines()

local_params = {}
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


print max(local_params.values())
