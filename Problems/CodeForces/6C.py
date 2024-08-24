n = int(input())
bars = list(map(int, input().split()))
a = 0
b = len(bars)-1
aBars = bBars = 0

while True:
    if a==b:
        print(aBars+1, bBars)
        break
    mn = min(bars[a], bars[b])

    bars[a] -= mn   
    bars[b] -= mn

    if bars[a] ==0:
        aBars+=1
        a+=1
        if a ==b:
            print(aBars, bBars+1)
            break
    if bars[b] == 0:
        bBars+=1
        b-=1
        if b ==a:
            print(aBars+1, bBars);
            break

