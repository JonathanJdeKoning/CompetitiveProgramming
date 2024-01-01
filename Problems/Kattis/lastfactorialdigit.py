tests = int(input())

for test in range(tests):
    num = int(input())
    total = 1
    
    
    for i in range(1,num +1):
        total*=i
    print(str(total)[-1])