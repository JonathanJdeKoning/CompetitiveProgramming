a = 0
b = 1
c = 1
while True:
    c += 1
    a,b = b,a+b
    if len(str(b)) == 1000:
        print(c)
        
