variations = set()


def do_replacement(molecule, recursion, replacement_keys):
    global replacements
    for char in replacement_keys:
        start = 0
        while molecule.find(char, start) is not -1:
            index = molecule.find(char, start)
            molecule_variation = molecule[:index] + replacements[char] + molecule[index + len(char):]
            global variations
            if molecule_variation == 'e':
                print recursion
                exit()
            elif molecule_variation not in variations:
                variations.add(molecule_variation)
                do_replacement(molecule_variation, recursion + 1, replacement_keys)
            start = index + 1

replacements = {}
molecule = ''
for line in file('input.txt'):
    line = line.strip()
    if ' => ' in line:
        char, replacement = line.split(' => ')
        replacements[replacement] = char
    else:
        molecule = line
replacement_keys = replacements.keys()[::-1]
do_replacement(molecule, 1, replacement_keys)
