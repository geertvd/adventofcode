import re

suspects_file = file('suspects.txt')
wanted_file = file('wanted.txt')

matches = [re.findall('(.+): (\d+)', line) for line in wanted_file]
wanted = dict(x[0] for x in matches if x)

sue_regex = re.compile('Sue (\d+): (.*)')

best_match = {
    'matches': 0,
    'number': 0
}
for line in suspects_file:
    suspect_raw = sue_regex.findall(line)[0]
    match = {
        'number': suspect_raw[0],
        'matches': 0
    }
    for suspect_property_raw in suspect_raw[1].split(', '):
        property_name, property_value = suspect_property_raw.split(': ')
        if property_name in wanted:
            operator = '=='
            if property_name in ['cats', 'trees']:
                operator = '>'
            elif property_name in ['pomeranians', 'goldfish']:
                operator = '<'

            if eval(property_value + ' ' + operator + ' ' + wanted[property_name]):
                match['matches'] += 1
            else:
                match['matches'] = 0
                break
    if match['matches'] > best_match['matches']:
        best_match = match
print best_match