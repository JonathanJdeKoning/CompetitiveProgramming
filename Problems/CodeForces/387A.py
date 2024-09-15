currH, currM = map(int, input().split(":"))
sleptH, sleptM = map(int, input().split(":"))

currH -= sleptH

if currH < 0:
    currH = 24 + currH

currM -= sleptM

if currM < 0:
    currM = 60+currM
    currH -= 1
    if currH == -1:
        currH = 23


print(f"{str(currH).zfill(2)}:{str(currM).zfill(2)}")
