import numpy as np
mat = []
badrows = []
badcols = []
with open("input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
    for i, line in enumerate(lines):
        linearr = [c for c in line]
        mat.append(linearr)
        if linearr.count("#") == 0:
            badrows.append(i)
new = np.rot90(mat,1)
mat = []
for i, line in enumerate(new):
    line = list(line)
    mat.append(line)
    if line.count("#") == 0:
        badcols.append(len(line)-i-1)
badcols = badcols[::-1]
new = np.rot90(mat,3)
mat = []
for line in new:
    mat.append(list(line))

#VISUALIZE
for line in mat:
    print("".join(line))

#BUILD NODES
nodes = []
for i, line in enumerate(mat):
    for j, spot in enumerate(line):
        if spot == "#":
            nodes.append([i,j])


sum = 0
#######################
#######################
                     ##
expan = 1000000      ##
                     ##
#######################
#######################
#print(f"{badrows=}")
#print(f"{badcols=}")
for node in nodes:
    for others in nodes:
        if others == node:
            continue
        dist = 0
        turn = 1
        miny=min([node[0],others[0]])
        maxy=max([node[0],others[0]])
        minx=min([node[1],others[1]])
        maxx=max([node[1],others[1]])
        passcols = list(range(minx, maxx))
        try:
            passcols.remove(minx)
        except: pass        
        try:
            passcols.remove(maxx)
        except:pass
        
        passrows = list(range(miny, maxy))
        
        try:
            passrows.remove(miny)
        except: pass
        
        try:
            passrows.remove(maxy)
        except:pass
        if miny!=maxy and minx!=maxx:
            dist+=turn
        badrowers = []
        badcollars = []

        for row in passrows:
            if row in badrows:
                badrowers.append(row)

        for col in passcols:
            if col in badcols:
                badcollars.append(col)
        inbetween = len(passrows) + len(passcols)
        numbads = len(badrowers) + len(badcollars)
        dist += inbetween
        dist -=numbads
        dist += numbads*expan
        dist+=1 

        #print(f"Node at {node[0]},{node[1]} going to {others[0]},{others[1]}\n\t passes through rows {passrows} and cols {passcols}\n\t it has badrows {badrowers} and badcols {badcollars}")
        #print(f"\t DISTANCE: {dist}")
        sum+=dist
print(sum//2)
