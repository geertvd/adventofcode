puzzle_input = open("day1/input.txt", "r").read()
puzzle_output = 0

input_length = len(puzzle_input)
steps_forward = input_length / 2
step = 0
for digit in puzzle_input:
    if digit == puzzle_input[(step + steps_forward) % input_length]:
        puzzle_output += int(digit)
    step += 1

print puzzle_output
