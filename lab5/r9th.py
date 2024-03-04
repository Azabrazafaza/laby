import re
def reg(s):
    patt = r'[A-Z]'
    t =""
    for i in range(len(s)):
        if re.match(patt , s[i]):
            t += " " + s[i]
        else:
            t += s[i]
    print(t)
s = str(input())
reg(s)