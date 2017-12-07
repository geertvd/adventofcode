puzzle_input = open("day5/input.txt", "r").read()
puzzle_output = 0

numbers = map(int, puzzle_input.split())

index = 0
while index < len(numbers):
    numbers[index] += 1
    index += numbers[index] - 1
    puzzle_output += 1

print puzzle_output
