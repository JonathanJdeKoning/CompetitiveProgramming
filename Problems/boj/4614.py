while True:
    poss = []
    s = input()
    if s == "#": break
    for i, c in enumerate(s):
        if c == ".":
            poss.append(100)
        elif c== "_":
            poss.append(0)
        elif c == "/":
            for j in range(i-1, -2,-1):
                if j ==-1: poss.append(100); break
                if s[j] == ".":
                    poss.append(100)
                    break
                elif s[j] == "|" or s[j] =="\\":
                    poss.append(0)
                    break

        elif c == "\\":
             for j in range(i+1, len(s)+1):
                if j ==len(s): poss.append(100);break
                if s[j] ==".":
                    poss.append(100)
                    break
                elif s[j] == "|" or s[j]=="/":
                    poss.append(0)
                    break

        elif c == "|":
            poss2 = []
            for j in range(i-1, -2,-1):
                if j ==-1: poss2.append(100); break
                if s[j] == ".":
                    poss2.append(100)
                    break
                elif s[j] == "|" or s[j] =="\\":
                    poss2.append(0)
                    break
            for j in range(i+1, len(s)+1):
                if j ==len(s): poss2.append(100);break
                if s[j]==".":
                    poss2.append(100)
                    break
                elif s[j] == "|" or s[j]=="/":
                    poss2.append(0)
                    break
            poss.append(sum(poss2)/2)
    print(int((sum(poss)/len(poss))//1))


