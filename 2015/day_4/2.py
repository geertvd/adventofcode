from sys import argv

script, input = argv

import hashlib
h = hashlib.md5()
h.update(input)
n = 0
hc = h.copy()

while not hc.hexdigest().startswith("000000"):
    hc = h.copy()
    hc.update(str(n))
    n += 1

print n - 1
