n,m,q = list(map(int, input().split()))

objs = []

for i in range(n):
    objs.append((input(),i+1))

for i in range(q):
    attr, truth = input().split()
    attr = int(attr)
    
    objs = [x for x in objs if x[0][attr-1] == truth]
    
if len(objs) == 1:
    print("unique")
    print(objs[0][1])
else:
    print("ambiguous")
    print(len(objs))
