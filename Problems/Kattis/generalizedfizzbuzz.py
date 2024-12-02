n,a,b = list(map(int, input().split()))
f = 0
g = 0
fg = 0

for i in range(1,n+1):
    if i%a==0 and i%b == 0:
        fg += 1
        continue
    if i%a == 0:
        f += 1
        continue
    if i%b == 0:
        g += 1


print(f,g,fg) 