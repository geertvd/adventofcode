puzzle_input = open("day1/input.txt", "r").read()
puzzle_output = 0

last_digit = puzzle_input[-1:]
for digit in puzzle_input:
    if last_digit == digit:
        puzzle_output += int(digit)
    last_digit = digit

print puzzle_output
