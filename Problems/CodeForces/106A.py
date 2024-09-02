t = input()

aR, aS, x , bR, bS = list(input())
d = {"6":0, "7":1, "8":2, "9":3, "T":4, "J":5, "Q":6, "K":7,"A":8}
if aS == t and bS!= t:
    print("YES")
elif aS==bS:
    if d[aR] > d[bR]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
