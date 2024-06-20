total = 0
n = int(input())
for i in range(1, n+1):
    if i<100: total += 1;continue
    if i==1000:break
    digs = [int(x) for x in str(i)]
    if digs[2]-digs[1] == digs[1]-digs[0]: total += 1
print(total)

