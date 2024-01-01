numints = int(input())
poss = list(range(1001))
for _ in range(numints):
    x, y = list(map(int, input().split()))
    period = list(range(x,y+1))
    poss = [x for x in poss if x in period]

if poss == []:
    print("edward is right")
else:
    print("gunilla has a point")
