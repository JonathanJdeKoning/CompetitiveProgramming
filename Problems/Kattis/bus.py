tests = int(input())

for i in range(tests):
    k = int(input())
    num = 0
    for i in range(k+1):
        num *=2
        num+=0.5
    print(int(num-0.5))
    
