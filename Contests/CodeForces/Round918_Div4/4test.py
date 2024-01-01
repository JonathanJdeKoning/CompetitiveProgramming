tc = int(input())
for _ in range(tc):
    slen = int(input())
    s = input()
    
    s = s.replace("bb", "b.b")
    s = s.replace("cc", "c.c")
    s = s.replace("dd", "d.d")
    s = s.replace("bc", "b.c")
    s = s.replace("cb", "c.b")
    s = s.replace("bd", "b.d")
    s = s.replace("db", "d.b")
    s = s.replace("dc", "d.c")
    s = s.replace("cd", "c.d")
    new = []
    for word in s.split("."):
        x = len(word)
        if x <=3:
            new.append(word)
            continue
        idx = 0
        while idx != (x-3) and idx != (x-2):
            new.append(word[idx:idx+2])
            idx+=2
        new.append(word[idx:])
    print(".".join(new))
