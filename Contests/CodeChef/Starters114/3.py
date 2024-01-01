import math
tc = int(input())

for _ in range(tc):
    n = int(input())

    s = input()
    needed = int(math.floor(n//2))+1
    neededx = n-needed
    
    for i,c in enumerate(s):
        if c == "R":
            neededx += 1
        if i == neededx:
            break
        
    pslap = neededx

    new = "P"*neededx

    x = "RPS"
    y = "PSR"
    table = str.maketrans(x,y)
    new+=s[neededx:].translate(table)
    
    if new.count("P") == len(new):
        new = "P"*n
    print(new)
