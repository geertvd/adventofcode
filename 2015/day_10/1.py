import itertools
from sys import argv
script, input, iterations= argv
for i in range(0,int(iterations)):
    num_groups = itertools.groupby(input)
    input = ''
    for dig,seq in num_groups:
        input += str(len(list(seq))) + str(dig)
print len(input)
