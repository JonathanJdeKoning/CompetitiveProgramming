
lines = "GFEDCBAgfedcba"
mp = {x:i for i, x in enumerate(lines)}
N= int(input())
notes = input().split()
need = (2*len(notes))-1
for note in notes:
    try: need += int(note[1:])-1
    except: pass
mat = [["-"]*need for _ in range(14)]

curr = 0
for note in notes:
    row = mp[note[0]]
    rep = 1
    if note[1:]: rep = int(note[1:])
    for i in range(rep):
        mat[row][curr] = "*"
        curr += 1
    curr += 1
bad = [0,2,4,6,8,10,11,12]
for i, row in enumerate(mat):
    if i in bad: row = "".join(row).replace("-", " ")
    else: row = "".join(row)
    print(lines[i]+": " + row)
    
