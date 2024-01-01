import math
matches, w, h = list(map(int, input().split()))

diag = math.sqrt(w*w+h*h)

for matchnum in range(matches):
    match = int(input())
    if match <= diag:
        print("DA")
    else:
        print("NE")
    