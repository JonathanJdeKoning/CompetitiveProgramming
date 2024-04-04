while True:
    n = int(input())
    if n == 0: break
    mn = 0
    mx = 999999999
    divs = []
    infinite = True
    for _ in range(n):
        data = input().split()
        if data[0] == "less":
            mx = min(mx, int(data[2]))
        elif data[0] == "greater":
            mn = max(mn, int(data[2]))
        elif data[0] == "divisible":
            divs.append(int(data[2]))
    if mx == 999999999: 
        print("infinite")
        continue
    poss = list(range(mn+1, mx))
    for div in divs:
        poss = [x for x in poss if x % div==0]
        
    if not poss:
        print("none")
        continue
    print(" ".join([str(x) for x in poss]))
    
