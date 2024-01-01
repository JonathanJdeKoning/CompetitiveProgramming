while True:
    try:
        text = input().split()
        #process text
        
        nums = []
        names = []
        for x in text:
            try:
                float(x)
                nums.append(float(x))
            except:
                names.append(x)
        print(f"{sum(nums)/len(nums)} {' '.join(names)}")
                
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    except EOFError:
        break