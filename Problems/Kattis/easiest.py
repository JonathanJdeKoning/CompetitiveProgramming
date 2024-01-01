while True:
    num = input()
    if num == "0": break
    numsum = sum([int(x) for x in num])

    counter = 11
    while True:
        
        testo = str(counter*int(num))
        if sum([int(x) for x in testo]) == numsum:
            print(counter)
            break
        counter += 1


