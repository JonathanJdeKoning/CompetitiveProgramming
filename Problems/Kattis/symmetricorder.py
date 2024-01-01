count = 1
while True:
    numclowns = int(input())
    if numclowns == 0: break

    clownsa = []
    clownsb = []
    togg = True
    for i in range(numclowns):
        if togg:
            clownsa.append(input())
        else: 
            clownsb.append(input())
        togg = not togg

    print(f"SET {count}")
    for clown in clownsa:
        print(clown)
    for clown in clownsb[::-1]:
        print(clown)
    count+=1
