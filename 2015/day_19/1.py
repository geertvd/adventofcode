replacements = {}
molecule = ''
for line in file('input.txt'):
    line = line.strip()
    if ' => ' in line:
        char, replacement = line.split(' => ')
        if char not in replacements:
            replacements[char] = []
        replacements[char].append(replacement)
    else:
        molecule = line
molecule_variations = set()
for char in replacements:
    start = 0
    while molecule.find(char, start) is not -1:
        index = molecule.find(char, start)
        for replacement in replacements[char]:
            molecule_variations.add(molecule[:index] + replacement + molecule[index + len(char):])
        start = index + 1

print len(molecule_variations)