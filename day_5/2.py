import re

rule_a = re.compile(r'(..).*\1')
rule_b = re.compile(r'(.).\1')

nice_string = 0
with open('input.txt') as fp:
    for line in fp:
        if not rule_a.findall(line):
              continue
        if rule_b.findall(line):
              nice_string += 1
print nice_string

