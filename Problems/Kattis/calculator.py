while True:
    try:
        string = input()
        print(f"{float(eval(string)):.2f}")
    except EOFError:
        break