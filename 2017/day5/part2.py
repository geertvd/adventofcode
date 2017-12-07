puzzle_input = open("day5/input.txt", "r").read()
puzzle_output = 0

numbers = map(int, puzzle_input.split())

index = 0
while index < len(numbers):
    offset = numbers[index]

    numbers[index] = numbers[index] + 1 if offset < 3 else numbers[index] - 1
    index += offset
    puzzle_output += 1

print puzzle_output
