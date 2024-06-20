for _ in range(int(input())):
    numBottles, numCritics = map(int, input().split())

    mxRed = 0
    mxWhite = 0
    for _ in range(numCritics):
        redWant, whiteWant = map(int, input().split())
        mxRed = max(mxRed, redWant)
        mxWhite = max(mxWhite, whiteWant)
    if mxRed+mxWhite > numBottles:
        print("IMPOSSIBLE")
    else:
        print(mxRed*"R" + mxWhite*"W" + (numBottles-(mxRed+mxWhite))*"W")
