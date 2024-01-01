tests = int(input())

for i in range(tests):
    num, upto = list(map(int, input().split()))
    
    pos, odd, eve = 0,0,0
    posc, oddc, evec = 0,0,0
    count = 1
    while evec != upto:
        if count %2 == 0:
            eve+=count
            evec+= 1
        else:
            odd += count
            oddc+=1
        
        if posc != upto:    
            pos += count
            posc += 1
        count +=1
    print(f"{num} {pos} {odd} {eve}")

