while True:
    a,b,x,y = input().split()
    
    p1 = a+b
    p2 = x+y
    if p1 == "00" and p2 == "00": break

    score1 = "".join(sorted(p1, reverse=True))
    score2 = "".join(sorted(p2, reverse=True))
    if score1 == "21":
        score1 = 999
    elif score1[0] == score1[1]:
        score1 = int(score1[0])*100
    else:
        score1 = int(score1)

    if score2 == "21":
        score2 = 999
    elif score2[0] == score2[1]:
        score2 = int(score2[0])*100
    else:
        score2 = int(score2)

    if score1 > score2:
        print("Player 1 wins.")
    elif score2 > score1:
        print("Player 2 wins.")
    else:
        print("Tie.")
