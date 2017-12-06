import re
input = file('input.txt').read()
findnumbers = re.compile('(-?\d+)')
print sum(map(int, findnumbers.findall(input)))
