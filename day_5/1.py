import re

vowel_check = re.compile('[aieuo]')
exclude_check = re.compile('ab|cd|pq|xy')
double_check = re.compile(r'(.)\1+')

nice_string = 0
with open('input.txt') as fp:
    for line in fp:
        if (len(vowel_check.findall(line)) < 3):
              continue
        if (exclude_check.findall(line)):
              continue
        if (double_check.findall(line)):
              nice_string += 1
print nice_string

