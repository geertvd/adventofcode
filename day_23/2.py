values = {
    'a': 1,
    'b': 0
}
operations = []
for line in file('input.txt'):
    line_parts = line.strip().replace(',', '').split(' ')
    if len(line_parts) == 2:
        line_parts.append(0)
    operations.append(line_parts)

i = 0
while i <= len(operations) - 1:
    op, a, b = operations[i]
    if op == 'hlf':
        values[a] /= 2
    elif op == 'tpl':
        values[a] *= 3
    elif op == 'inc':
        values[a] += 1
    elif op == 'jmp':
        i = i + int(a[1:]) if a[:1] == '+' else i - int(a[1:])
        continue
    elif (op == 'jie' and values[a] % 2 == 0) or (op == 'jio' and values[a] == 1):
        i = i + int(b[1:]) if b[:1] == '+' else i - int(b[1:])
        continue

    i += 1

print values
