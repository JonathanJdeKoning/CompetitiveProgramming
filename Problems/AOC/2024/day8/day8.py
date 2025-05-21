ans1 = 0    
ans2 = 0    

mat = [list(line.strip()) for line in open("day8.in", "r")]
from collections import defaultdict

mp = defaultdict(list)
R, C = len(mat), len(mat[0])
for i in range(R):
    for j in range(C):
        if mat[i][j] != ".":
            mp[mat[i][j]].append((i,j))
ant = set()
for nodeType, nodes in mp.items():
    for i in range(len(nodes)-1):
        aY, aX = nodes[i] 
        for j in range(i+1, len(nodes)):
            mul = 0
            bY, bX = nodes[j]
            while True:
                antY = mul*((aY-bY)) + aY
                antX = mul*((aX-bX)) + aX
                if min(antY, antX) <=-1 or antY >= R or antX >= C:
                    break
                else:
                    ant.add((antY, antX))
                    mul += 1
            mul = 0
            while True:
                antY = mul*((bY-aY)) + bY
                antX = mul*((bX-aX)) + bX
                if min(antY, antX) <=-1 or antY >= R or antX >= C:
                    break
                else:
                    ant.add((antY, antX))
                    mul += 1
for y,x in ant:
    mat[y][x] = "#"
print("\n".join([" ".join(map(str, row)) for row in mat ]))

print(ant)
print(len(ant))
