s = input()

if "0" not in s: print(s[1:])
else:
    print(s[:s.index("0")] + s[s.index("0")+1:])
