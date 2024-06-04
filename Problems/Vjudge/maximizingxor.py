l = int(input())
r = int(input())
mx =0 
for i in range(l,r+1):
    for j in range(l, r+1):
        mx =max(mx, i^j)
print(mx)
