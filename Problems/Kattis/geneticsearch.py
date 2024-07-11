import re
while True:
    try:
        s, l = input().split()
    except: break
    seen = set()
    a = len(re.findall(f"(?={s})",l))
    seen.add(a)
    b = 0
    c = 0
    for i, cell in enumerate(s):
        sub = s[:i] + s[i+1:]
        if sub not in seen:
            b += len(re.findall(f"(?={sub})",l))
            seen.add(sub)

        for letter in "ACTG":
            sub = s[:i]+ letter + s[i:]
            if sub not in seen:
                c += len(re.findall(f"(?={sub})",l))
                seen.add(sub)
        for letter in "ACTG":
            sub = s+ letter
            if sub not in seen:
                c += len(re.findall(f"(?={sub})",l))
                seen.add(sub)


    print(a,b,c)
