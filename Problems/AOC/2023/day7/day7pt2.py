from collections import Counter as C
s={"A":1,"K":2,"Q":3,"T":4,"9":5,"8":6,"7":7,"6":8,"5":9,"4":10,"3":11,"2":12,"J":13}
bids,hs,sum={},[],0
with open("input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
    for line in lines:
        h,bid=line.split()
        bids[h]=int(bid)
        hs.append(h)
mult=len(hs)
fi=[h for h in hs if 5 in C(h).values()]
fo=[h for h in hs if 4 in C(h).values()]
fu=[h for h in hs if 3 in C(h).values()and 2 in C(h).values()]
t=[h for h in hs if 3 in C(h).values()and 1 in C(h).values()]
ps=[h for h in hs if list(C(h).values()).count(2)==2]
tw=[h for h in hs if list(C(h).values()).count(2)==1 and list(C(h).values()).count(1)==3]
o=[h for h in hs if len(C(h).values())==5]

for h in fo[::-1]:
    if "J" in h:
        fi.append(h)
        fo.remove(h)

for h in fu[::-1]:
    if "J" in h:
        fi.append(h)
        fu.remove(h)

for h in t[::-1]:
    if "J" in h:
        fo.append(h)
        t.remove(h)

for h in ps[::-1]:
    if h.count("J")==2:
        fo.append(h)
        ps.remove(h)
    elif h.count("J")==1:
        fu.append(h)
        ps.remove(h)

for h in tw[::-1]:
    if "J" in h:
        t.append(h)
        tw.remove(h)

for h in o[::-1]:
    if "J" in h:
        tw.append(h)
        o.remove(h)

fi = sorted(fi,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
fo = sorted(fo,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
fu = sorted(fu,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
t = sorted(t,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
ps= sorted(ps,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
tw = sorted(tw,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
o = sorted(o,key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))

for h in fi+fo+fu+t+ps+tw+o:
    sum+=bids[h]*mult
    mult-=1
print(sum)
