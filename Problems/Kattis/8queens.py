
def solve():
    mat = []
    for _ in range(8):
        mat.append(list(input()))

    for row in mat:
        if row.count("*")!=1: return "invalid"
    
    for i in range(8):
        if [x[i] for x in mat].count("*")!=1: return "invalid"
    
    for i, row in enumerate(mat):
        for j, x in enumerate(row):
            if x == "*":
                dy = i
                dx = j
                while dy != 7 and dx != 7:
                    dy+=1
                    dx+=1 
                    if mat[dy][dx] == "*": return "invalid"
                
                dy = i
                dx = j
                while dy != 7 and dx != 0:
                    dy+=1
                    dx-=1 
                    if mat[dy][dx] == "*": return "invalid"
    return "valid"
                
print(solve())



               
