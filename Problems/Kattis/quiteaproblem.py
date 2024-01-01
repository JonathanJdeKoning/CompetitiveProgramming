while True:
    try:
        text = input().lower()
        if "problem" in text:
            print("yes")
        else:
            print("no")
    
    except EOFError:
        break