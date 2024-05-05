s = input()

if s[0].islower() and len([x for x in s[1:] if x.islower()]) == 0:
    print(s[0].upper() + s[1:].lower())
else:
    if len([x for x in s if x.islower()]) == 0:
        print(s.lower())
    else:
        print(s)
