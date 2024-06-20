for n in range(int(input())):
    s = input()
    best = s
    pref = []
    for i,c in enumerate(s):
        new = "".join(pref)+c+c+s[i+1:]
        if new < best:
            best = new
            pref.append(c)
        pref.append(c)
    print(f"Case #{n+1}: {best}")
        


    
        
