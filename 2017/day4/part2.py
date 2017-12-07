puzzle_input = open("day4/input.txt", "r")
puzzle_output = 0

for line in iter(puzzle_input.readline, b''):
    words = line.split()

    for index, word in enumerate(words):
        words[index] = ''.join(sorted(word))

    if len(words) == len(set(words)):
        puzzle_output += 1

print puzzle_output
