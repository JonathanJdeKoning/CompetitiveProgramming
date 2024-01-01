while True:
    numwords = int(input())
    if numwords == 0:
         break
    words = [input() for _ in range(numwords)]
    maxi = -1
    biggy = ""
    for word in words:
        total = word.count("aa") + word.count("ee") + word.count("ii") + word.count("oo") + word.count("uu") + word.count("yy") 
        if total > maxi:
            maxi = total
            biggy = word
    print(biggy)
