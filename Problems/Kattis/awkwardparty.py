n,d=int(input()),{}
s,m=map(int,input().split()),n
for i,c in enumerate(s):
    if c not in d:
        d[c]=i
    else:
        m=min(m,i-d[c]);d[c]=i
print(m)
