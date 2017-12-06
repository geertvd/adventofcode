from sys import argv
script, wire_input = argv
txt = open('input.txt')

wires = {}
operators = {
    'AND': '&',
    'OR': '|',
    'LSHIFT': '<<',
    'RSHIFT': '>>'
}

for line in txt:
    line = line.strip()
    signal, wire = line.split(' -> ')
    wires[wire] = signal

wire_values = {}

def wiresignal( wire, wires, wire_values ):
    if wire_values.get(wire):
        return wire_values.get(wire)

    signal = wires[wire]
    if signal.isdigit():
        wire_values[wire] = signal
        return int(signal)
    sp = signal.split(' ')
    if len(sp) == 1:
        return wiresignal(sp[0], wires, wire_values)
    elif len(sp) == 2:
        return - wiresignal(sp[1], wires, wire_values) % 65535
    else:
        x, op, y = sp
        x = x if x.isdigit() else wiresignal(x, wires, wire_values)
        y = y if y.isdigit() else wiresignal(y, wires, wire_values)
        wire_values[wire] = eval(str(x) + ' ' + operators[op] + ' ' + str(y))
        return wire_values[wire]

response = wiresignal( wire_input, wires, wire_values)
print response
