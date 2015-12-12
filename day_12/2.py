import json
import re
input = json.load(file('input.txt'))

findnumbers = re.compile('(-?\d+)')

def countjson(o):
    count = 0
    for oo in o:
        oo = o.get(oo) if type(o) is dict else oo
        if type(o) is dict and oo == 'red':
            return 0
        elif isinstance(oo, int):
            count += oo
        elif type(oo) is list or type(oo) is dict:
            count += countjson(oo)
    return count

print countjson(input)
