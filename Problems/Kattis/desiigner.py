import re
pat = "br{2,}[aeiouy]"
s = input()
if re.match(pat, s):
    print("Jebb")
else:
    print("Neibb")