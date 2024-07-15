while True:
    try:
        n = int(input())
    except: break
    guess = "1"
    while True:
        if int(guess)%n==0:
            print(len(guess))
            break
        guess += "1"
