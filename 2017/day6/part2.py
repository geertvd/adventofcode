puzzle_input = map(int, open("day6/input.txt", "r").read().split())
puzzle_output = 0


def find_key(list, value):
    for index, item in enumerate(list):
        if item == value:
            return index
    return 0


def distribute_blocks(banks):
    num_banks = len(banks)
    available_blocks = max(banks)
    bank_index = find_key(banks, available_blocks)
    banks[bank_index] = 0
    while available_blocks:
        bank_index += 1
        banks[bank_index % num_banks] += 1
        available_blocks -= 1
    return banks


distribution_archive = []
while len(distribution_archive) == len(set(distribution_archive)):
    puzzle_input = distribute_blocks(puzzle_input)
    distribution_archive.append(''.join(map(str, puzzle_input)))

loop_start = distribution_archive[-1]

while True:
    puzzle_input = distribute_blocks(puzzle_input)
    puzzle_output += 1
    if loop_start == ''.join(map(str, puzzle_input)):
        break

print puzzle_output