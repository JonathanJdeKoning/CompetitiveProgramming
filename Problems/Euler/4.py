mx = 0
for i in range(100,1000):
    for j in range(100,1000):
        x = str(i*j)
        if x == x[::-1]:
            mx = max(mx, int(x))
print(mx) 
