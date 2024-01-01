tests = int(input())


for test in range(tests):
    datanum, days = list(map(int, input().split()))

    total = 0
    
    for i in range(1,days+1):
        total += 1 + i
    print(str(datanum) + " " + str(total))
    