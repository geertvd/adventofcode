input_lengths = map(ord, open("day10/input.txt", "r").read())
input_lengths += [17, 31, 73, 47, 23]
circular_list_length = 256
circular_list = range(circular_list_length)
current_position = 0
skip_size = 0
rotations = 0

while rotations < 64:
    rotations += 1
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

block = 0
dense_hash = []
while block < 16:
    sparse_hash_block = circular_list[block * 16:(block + 1) * 16]
    dense_hash_block = sparse_hash_block[0]
    for number in sparse_hash_block[1:]:
        dense_hash_block = dense_hash_block ^ number

    dense_hash.append(dense_hash_block)
    block += 1

dense_hash_string = ''
for number in dense_hash:
    dense_hash_string += format(number, '02x')

print dense_hash_string