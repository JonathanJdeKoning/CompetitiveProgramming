q = input().split()

tit = q[0]
maxi = float(q[1])

if len(tit) > maxi:
    print(maxi)
else:
    print(len(tit))