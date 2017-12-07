puzzle_input = 347991
puzzle_output = 0


def calc_adjacent_sum(matrix, x, y):
    adjacent_sum = matrix[x + 1][y] + matrix[x + 1][y + 1] + matrix[x][y + 1] + matrix[x - 1][y + 1] + matrix[x - 1][y] + matrix[x - 1][y - 1] + matrix[x][y - 1] + matrix[x + 1][y - 1]
    return adjacent_sum

matrix = [[0 for i in range(1000)] for j in range(1000)]
x = x_max = x_min = 500
y = y_max = y_min = 500
matrix[x][y] = 1
layer = next_corner = 0
layer_start = layer_end = position = 1
top_right = bottom_left = False
while True:
    position += 1

    if position > layer_end:
        layer += 1
        layer_start = layer_end
        layer_end += 8 * layer
        layer_length = layer_end - layer_start
        layer_side_length = (layer_length + 4) / 4
        y_max = x_max = 500 + (layer_side_length - 1) / 2
        x_min = y_min = 500 - (layer_side_length - 1) / 2
        x += 1
        matrix[x][y] = calc_adjacent_sum(matrix, x, y)
        top_right = True
        bottom_left = False
        continue

    if top_right:
        if y < y_max:
            y += 1
        elif x > x_min:
            x -= 1
        else:
            top_right = False
            bottom_left = True
    if bottom_left:
        if y > y_min:
            y -= 1
        elif x < x_max:
            x += 1
        else:
            bottom_left = False
            top_right = False

    matrix[x][y] = calc_adjacent_sum(matrix, x, y)
    if matrix[x][y] > puzzle_input:
        print matrix[x][y]
        break
