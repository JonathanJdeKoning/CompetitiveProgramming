h, w = list(map(int, input().split()))
matrix = []

for i in range(h):
    matrix.append(input())

res = [0,0,0,0,0]
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        out = ""
        
        try:
            out += matrix[i][j]
            out += matrix[i][j+1]
            out += matrix[i+1][j]
            out += matrix[i+1][j+1]

            if "#" in out:
                continue
            
            
            res[out.count("X")] += 1
        except:
            continue
print("\n".join([str(x) for x in res]))
