cases = int(input())

for case in range(cases):
    sounds = input().split()
    
    line = ""
    
    while line != "what does the fox say?":
        line = input()
        animalsound = line.split()[2]
        
        sounds = [i for i in sounds if i != animalsound]
    print(" ".join(sounds))
        