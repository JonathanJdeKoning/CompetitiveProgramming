ans = 0
mat = []
with open("sample.txt", "r") as file:
    for line in file.readlines():
        mat.append(["."] + list(line.strip()) + ["."])

R, C = len(mat)+2, len(mat[0])
mat = ["."*C] + mat
mat.append(["."]*C)
for row in mat: print(" ".join(map(str, row)))

directions = [(x,y) for x in (-1,0,1) for y in (-1,0,1) if (x,y) != (0,0)]
seen = set()
for i in range(R):
    for j in range(C):
        if (i,j) in seen: continue
        if not mat[i][j].isdigit(): continue
        curr = j
        num = []
        while mat[i][curr].isdigit():
            num.append(mat[i][curr])
            seen.add((i,curr))
            curr += 1
        surr = []
        surr.append(mat[i][j-1])
        surr.append(mat[i][j+len(num)+1])
        surr.extend(mat[i-1][j-1:j+len(num)+1])
        surr.extend(mat[i+1][j-1+len(num)+1])
        if len(surr) != surr.count("."):
            good = int("".join(num))
            ans += good
            print(good)
print(ans)