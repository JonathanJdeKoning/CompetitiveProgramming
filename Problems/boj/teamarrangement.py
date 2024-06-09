done = False
begin = True
while True:
    players = []
    for _ in range(22):
        data = input().split()
        if data == ["0"]: done=True;break
        data[0] = int(data[0])
        players.append(data)
    if done: break
    out =[]
    d,m,s = map(int, input().split("-"))
    g = 1
    
    dArr = []
    mArr = []
    sArr = []
    gArr = []

    for player in sorted(players):
        id = player[2]
        if id == "D" and d >0:
            dArr.append(player); d-=1
        if id == "M" and m >0:
            mArr.append(player); m-=1
        if id == "S" and s >0:
            sArr.append(player); s-=1
        if id == "G" and g >0:
            gArr.append(player); g-=1

    out.extend(gArr)
    out.extend(dArr)
    out.extend(mArr)
    out.extend(sArr)
    
    mxYears = 0 
    for player in out:
        years = player[3:]
        total = 0
        for year in years:
            start,end = year.split("-")
            total += (int(end)-int(start)) +1
        if total > mxYears:
            mxYears = total
            captain = player
        elif total == mxYears:
            if player[0]> captain[0]:
                captain = player

    capPos = captain[2]
    out.remove(captain)
    out = [captain] + out
    if g or d or s or m:
        print("IMPOSSIBLE TO ARRANGE")
    else:
        for player in out:
            print(" ".join([str(x) for x in player[:3]]))

