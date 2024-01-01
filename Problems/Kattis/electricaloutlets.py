tests = int(input())

for test in range(tests):
    testlist = list(map(int, input().split()))
    
    strips = testlist[0]
    outlets = testlist[1:]
    
    total = sum([x-1 for x in outlets])+1
    print(total)
    
    