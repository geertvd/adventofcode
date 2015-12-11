import re
import string
from sys import argv
script, password = argv

def isvalid(password):
    doubles = re.compile(r'([a-z])\1').findall(password)
    combofound = False
    for i in range(0, len(password)-2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
            combofound = True
            break;

    if not combofound:
        return False
    if len(doubles) < 2:
        return False
    if re.compile('[iol]').findall(password):
        return False
    return True

def increment_password(password):
    reversed_pw = list(password[::-1])
    for pos, c in enumerate(reversed_pw):
        asci = ord(c) + 1
        nc = chr(asci) if asci <= 122 else 'a'
        reversed_pw[pos] = nc
        if nc != 'a':
            break;
    return ''.join(reversed_pw[::-1])

new_password = increment_password(password)
while not isvalid(new_password):
    new_password = increment_password(new_password)

print new_password
