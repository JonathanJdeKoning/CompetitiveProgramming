tests = int(input())

for test in range(tests):
    gnomelist = list(map(int, input().split()))
    listlen = gnomelist[0]
    gnomelist = gnomelist[1:]
    gnomestart = gnomelist[0] 
    
    count = 0
    for gnome in range(gnomestart, gnomestart+listlen):
        count += 1
        if gnome != gnomelist[count-1]:
            print(count)
            break
    