a,b,c = list(map(int,input().split()))

x = list(map(int, input().split()))
x = list(range(x[0],x[1]))
y = list(map(int, input().split()))
y = list(range(y[0],y[1]))
z = list(map(int, input().split()))
z = list(range(z[0],z[1]))

length = max([x[-1],y[-1],z[-1]])
tot = 0
for i in range(1, length+1):
    count = 0
    if i in x:
        count += 1
    if i in y:
        count += 1
    if i in z:
        count += 1

    if count == 1:
        tot += a
    if count == 2:
        tot += b*2
    if count == 3:
        tot += c*3
print(tot)    
