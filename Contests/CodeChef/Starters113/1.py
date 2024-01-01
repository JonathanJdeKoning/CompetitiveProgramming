bad = [1,2,5]
tc = int(input())
for _ in range(tc):
    n = int(input())
    
    if n not in bad:
        print("YES")
    else:
        print("NO")

