import re
def reg(s):
    patt = r'[ ,.]+'
    print(re.sub(patt , ':' , s))
s = str(input())
reg(s)
