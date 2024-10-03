yo = []
good = set(list("0123456789abcdefABCDEF"))
while True:
    try:
        s = input().encode("utf-8")
    except EOFError: break
    s = s.replace("0x", "©").replace("0X", "®")
    print(s)
    for i, c in enumerate(yo):
        if c in "©®":
            print(i)
            """
            if i!= len(s)-1 and s[i+1] in good:
                seek = i+1
                while True:
                    if s[seek] in good:
                        pass
            """ 