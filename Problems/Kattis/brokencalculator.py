calcs = int(input())
prev = 1
for _ in range(calcs):
    data = input().split()
    x = int(data[0])
    y = int(data[2])
    op = data[1]
    
    if op == "+":
        res = (x+y) - prev
        prev = res
        print(res)
    if op == "-":
        res = (x-y)*prev
        prev = res
        print(res)
    if op == "*":
        res = (x*y)**2
        prev = res
        print(res)
    if op == "/":
        if x%2 == 0:
            res = x//2
        else:
            res = (x+1)//2
        prev = res
        print(res)
    
