import re
def reg(s):
    patt = r'a.+b'
    if re.search(patt , s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('good')
else:
    print('no')