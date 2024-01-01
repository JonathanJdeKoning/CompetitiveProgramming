tc = int(input())
for _ in range(tc):
    n = int(input())//2
    s = input().replace(" ", "")
    score = 0
    
    while True:
        num = s.count("01")
        s = s.replace("01", "")
        score += num
        
        num2 = s.count("10")
        s = s.replace("10", "")
        score += num2
        
        if num == 0 and num2 == 0:
            break
    print(score)

    

