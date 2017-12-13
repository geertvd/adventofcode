input_lengths = map(int, open("day10/input.txt", "r").read().split(','))
circular_list_length = 256
circular_list = range(circular_list_length)
current_position = 0
skip_size = 0
for input_length in input_lengths:
    if input_length:
        stop = current_position + input_length
        if current_position + input_length > circular_list_length:
            stop = (current_position + input_length) % circular_list_length
            sub_list = circular_list[current_position:] + circular_list[:stop]
        else:
            sub_list = circular_list[current_position:stop]

        sub_list = sub_list[::-1]
        if current_position < stop:
            circular_list[current_position:stop] = sub_list
        else:
            circular_list[current_position:] = sub_list[:circular_list_length - current_position]
            circular_list[:stop] = sub_list[circular_list_length - current_position:]

    if len(circular_list) != circular_list_length:
        print input_length
        break

    current_position = (current_position + input_length + skip_size) % circular_list_length
    skip_size += 1

print circular_list[0] * circular_list[1]
