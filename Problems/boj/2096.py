n = int(input())
from math import inf
mx = [0,0,0]
mn = [0,0,0]
for i in range(n):
    new = list(map(int, input().split()))
    newmx = [0,0,0]
    newmn = [0,0,0]
    for j in range(3):
        if j==0:
            newmx[j] = new[j] + max(mx[0], mx[1])
            newmn[j] = new[j] + min(mn[0], mn[1])
        elif j==2:
            newmx[j] = new[j] + max(mx[2], mx[1])
            newmn[j] = new[j] + min(mn[2], mn[1])
        elif j==1:
            newmx[j] = new[j] + max(mx[0], mx[1], mx[2])
            newmn[j] = new[j] + min(mn[0], mn[1], mn[2])
    mn = newmn[:]
    mx = newmx[:]
print(max(mx), min(mn))


