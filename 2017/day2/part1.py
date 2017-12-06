puzzle_input = open("day2/input.txt", "r")
puzzle_output = 0

for line in iter(puzzle_input.readline, b''):
    digits = line.split()
    max_digit = min_digit = int(digits[0])
    for digit in digits:
        digit = int(digit)
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
    puzzle_output += max_digit - min_digit

print puzzle_output
