my = list(map(int,input().split()))

while my != [1,2,3,4,5]:
    if my[0] > my[1]: 
        my[0],my[1] = my[1],my[0]
        print(" ".join([str(x) for x in my]))

    if my[1] > my[2]: 
        my[1],my[2] = my[2],my[1]
        print(" ".join([str(x) for x in my]))

    if my[2] > my[3]: 
        my[2],my[3] = my[3],my[2]
        print(" ".join([str(x) for x in my]))

    if my[3] > my[4]: 
        my[3],my[4] = my[4],my[3]
        print(" ".join([str(x) for x in my]))

