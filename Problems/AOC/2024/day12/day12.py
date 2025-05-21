from collections import defaultdict
mat = [list(line.strip()) for line in open("day12.in", "r")]
per = defaultdict(int)
area = defaultdict(int)
R, C = len(mat), len(mat[0])
seen = set()
ans1 =0
ans2 = 0
directions = [(-1,0),(0,1),(1,0),(0,-1)]
sidedirs = {(0,1), (0,-1)}
for i in range(R):
    for j in range(C):
        if (i,j) in seen: continue
        mine = set()
        dfs = [(i,j)]
        per = 0
        area = 0
        out = set()
        while dfs:
            currY, currX = dfs.pop()

            if (currY, currX) in seen: continue
            area += 1
            seen.add((currY, currX))
            mine.add((currY, currX))

            for dy, dx in directions:
                y,x = dy+currY, dx+currX
                
                if y == -1 or y == R:
                    per += 1
                    out.add((y, (dy,dx)))
                    continue
                if x == -1 or x == C:
                    per += 1
                    out.add((x, (dy, dx)))
                    continue
                if mat[y][x] != mat[i][j]:
                    per += 1
                    if (dy, dx) in sidedirs:
                        out.add((x, (dy, dx)))
                    else:
                        out.add((y, (dy,dx)))
                    continue
                if (y,x) in seen:
                    continue
                dfs.append((y,x))

        sides = 0
        
        out = list(out)
        for start, (ndy, ndx) in out:
            vdy, vdx = -ndy, -ndx
            poss = True
            if ndy == 0:
                for k in range(C):
                    if ((k, start) in mine and (k-1, start) not in mine) or ((k, start) not in mine and (k+vdy, start+vdx) not in mine):
                        poss = True
                        continue
                    if poss and (k, start) not in mine and (k+vdy, start+vdx) in mine:
                        sides += 1
                        poss = False
            else:
                for k in range(R):
                    if (start,k) in mine and (start, k-1) not in mine or ((start, k) not in mine and (start+vdy, k+vdx) not in mine):
                        poss = True
                        continue
                    if poss and (start, k) not in mine and (start+vdy, k+vdx) in mine:
                        sides += 1
                        poss = False
        
        ans1 += area*per
        ans2 += area*sides

print(ans1)
print(ans2)

                    

            



        
