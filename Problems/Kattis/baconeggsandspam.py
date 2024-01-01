while True:
    names = []
    foods = []
    history = []
    lines = int(input())
    
    if lines == 0:
        break
    for _ in range(lines):
        string = input().split()
        name = string[0]
        food = string[1:]
        
        names.append(name)
        for yum in food:
            foods.append(yum)
        history.append(string)
        
    names = set(names)
    foods = sorted(set(foods))    
    
    
    for yum in foods:
        whoeated = []
        for hist in history:
            if yum in hist:
                whoeated.append(hist[0])
    
        print(f"{yum} {' '.join(sorted(whoeated))}")
    print()
            
    
    
    
    