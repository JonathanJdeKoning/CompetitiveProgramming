import itertools
def prefixes(iterable):
    return list(itertools.accumulate(map(lambda x: x, iterable[:-1])))
data = input().split()
a = data[0]
b = data[2]
c = data[4]
op = data[1]
alen = len(a)
blen = len(b)
clen = len(c)
possible = []

aprefs = prefixes(a)
bprefs = prefixes(b)
cprefs = prefixes(c)

for apref in aprefs:
    for bpref in bprefs:
        newa = bpref + a[len(apref):]
        newb = apref + b[len(bpref):]

        possible.append(" ".join([newa,op,newb,"==",c]))

for apref in aprefs:
    for cpref in cprefs:
        newa = cpref + a[len(apref):]
        newc = apref + c[len(cpref):]

        possible.append(" ".join([newa,op,b,"==",newc]))

for cpref in cprefs:
    for bpref in bprefs:
        newc = bpref + c[len(cpref):]
        newb = cpref + b[len(bpref):]

        possible.append(" ".join([a,op,newb,"==",newc]))
for poss in possible:
    if eval(poss):
        poss = poss.replace("==","=")
        print(poss)
