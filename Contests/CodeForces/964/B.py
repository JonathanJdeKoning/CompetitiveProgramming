def solve():
    a1,a2,b1,b2 = map(int, input().split())
    ways = 0
    
    poss = [[(a1,b1),(a2,b2)],[(a1,b2),(a2,b1)],[(a2,b1),(a1,b2)],[(a2,b2),(a1,b1)]]

    for game in poss:
        apoints = 0
        bpoints = 0

        for acard, bcard in game:
            if acard > bcard:
                apoints += 1
            elif bcard> acard:
                bpoints += 1
        if apoints > bpoints:
            ways += 1
    return ways
    
for _ in range(int(input())):
    print(solve())
