from itertools import dropwhile, takewhile
import re
pattern = re.compile("da+dd?(i|y)")
while True:
    try:
        s = input()
    except EOFError: break

    if not s.startswith("da"):
        print("Cooing")
        continue
    
    s = list(dropwhile(lambda x: x=="a", list(s)[1:]))
    if s[0] != "d":
        print("Cooing")
        continue

    s = s[1:]

    if len(s) == 1:
        if s[0] not in "iy":
            print("Cooing")
            continue
    elif len(s) == 2:
        if s[0] != "d":
            print("Cooing")
            break
        else:
            if s[-1] not in "iy":
                print("Cooing")
                continue
    else:
        print("Cooing")
        continue
    print("She called me!!!")


