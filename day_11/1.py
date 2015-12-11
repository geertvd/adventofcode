import re
import string
from sys import argv
script, password = argv

def isvalid(password):
    doubles = re.compile(r'([a-z])\1').findall(password)
    alphabet = list(string.ascii_lowercase)
    combofound = False
    for i,letter in enumerate(alphabet[:-2]):
        combo = ''.join(alphabet[i:i+3])
        if combo in password:
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
