for _ in range(int(input())):
    n = input()
    out = []
    print(len([x for x in n if x != "0"]))
    for i,c in enumerate(n):
        if c != "0":
            
            out.append(c+"0"*((len(n)-1)-i))
    print(" ".join(out))
