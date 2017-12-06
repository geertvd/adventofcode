puzzle_input = open("day2/input.txt", "r")
puzzle_output = 0

for line in iter(puzzle_input.readline, b''):
    digits = line.split()
    max_digit = min_digit = int(digits[0])
    for digit_a in digits:
        for digit_b in digits:
            if digit_a == digit_b:
                continue

            divided = float(digit_a) / float(digit_b)
            if divided.is_integer():
                puzzle_output += divided
                break

print puzzle_output
