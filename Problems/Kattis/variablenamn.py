numvars = int(input())
seen = []

for _ in range(numvars):
    new = int(input())
    if new not in seen:
        print(new)
        seen.append(new)
    else:
        count = 2
        while True:
            test = count*new 
            if test not in seen:
                print(test)
                seen.append(test)
                break
            else:
                count+=1
