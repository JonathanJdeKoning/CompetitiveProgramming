for _ in range(int(input())):
    poss = []
    want = input()
    a = input()
    b = input()
    c = input()
    d = input()
    
    for test in [a,b,c,d]:
        for i in range(min(len(test), len(want))):
            if test[i] != want[i]: break
        else:
            i+=1

        comPref = i
        need = (len(test)  - comPref) + (len(want) - comPref)
        if test != a:
            poss.append(need + 1)
        else:
            poss.append(need)
    #print(poss)
    print(min(poss))