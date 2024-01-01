tests = int(input())

for test in range(tests):
    num = int(input())
    numsum = sum([int(x) for x in str(num)])
    
    for i in range(num, -1, -1):
        i = str(i)
        isum = sum([int(c) for c in str(i)])
        
        if isum == numsum-1:
            print(i)
            break
