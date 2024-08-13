for a in range(1,1001):
    print(a)
    for b in range(a,1001):
        for c in range(b,1001):
            if a+b+c !=1000: continue
            if a**2+b**2==c**2:
                print(a*b*c)
                break
            
