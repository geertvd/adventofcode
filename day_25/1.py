search = [3029, 2947]
num_value = sum(range(search[0] + search[1])) - search[1] + 1
prev_value = 20151125
while num_value > 1:
    prev_value = (prev_value * 252533) % 33554393
    num_value -= 1

print prev_value