import math

poss = list(range(1,1001))
for i in range(10):
    try:
        print(poss[int(math.ceil(len(poss)/2))]-1, flush=True)
    except:
        print(1000)
    ans = input()
    
    if ans == "correct":
        break
    elif ans == "higher":
            poss = poss[int((math.ceil(len(poss)/2))):]
    elif ans == "lower":
        poss = poss[:int(math.ceil(len(poss)/2))]