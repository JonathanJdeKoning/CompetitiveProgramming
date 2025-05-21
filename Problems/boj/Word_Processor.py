N, K = list(map(int, input().replace(","," ").split()))
para = []
curr = K
row = []
for word in input().split():
    n = len(word)
    if n <= curr:
        curr -= n
        row.append(word)
    else:
        para.append(row)
        row = [word]
        curr = K - n  
if row:
    para.append(row)
for row in para:
    print(*row)