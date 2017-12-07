puzzle_input = 347991
puzzle_output = 0

layer = 0
layer_increment = 0
layer_end = 1

while puzzle_input > layer_end:
    layer += 1
    layer_increment = 8 * layer
    layer_end += layer_increment

# +4 since the corners are re-used.
side_length = ((layer_end - (layer_end - layer_increment)) + 4) / 4
side_middle = (side_length + 1) / 2

for side in range(0, 4):
    middle_number = layer_end - (side_middle - 1) - side_length * side + 1 * side
    if puzzle_input >= middle_number:
        puzzle_output = layer + puzzle_input - middle_number
        break
    elif side == 3:
        puzzle_output = layer + middle_number - puzzle_input

print puzzle_output
