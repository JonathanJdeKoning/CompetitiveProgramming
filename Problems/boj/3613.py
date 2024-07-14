s = input()
if s[-1] == "_" or s[0] == "_" or "__" in s or s[0] == s[0].upper():
    print("Error!")

elif "_" in s:
    if len([x for x in s.replace("_","") if x == x.upper()]) != 0:
        print("Error!")
    else:
        words = s.split("_")
        for i in range(1,len(words)):
            words[i] = words[i].title()
        print("".join(words))
else:
    if len([x for x in s if x == x.upper()]) == 0:
        print(s)
    else:
        words = []
        new =[]
        for c in s:
            if c == c.upper():
                words.append("".join(new))
                new = [c.lower()]
            else:
                new.append(c)
        words.append("".join(new))
        print("_".join(words))
