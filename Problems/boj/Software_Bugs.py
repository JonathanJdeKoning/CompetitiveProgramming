while True:
    try:
        s = input()
    except EOFError: break

    while "BUG" in s:
        s = s.replace("BUG", "")
    print(s)