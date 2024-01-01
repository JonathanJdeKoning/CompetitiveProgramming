vars = {}
while True:
    try:
        command = input().split()
        if command[0] == "define":
            vars[command[2]] = int(command[1])
        elif command[0] == "eval":
            try:
                x = vars[command[1]]
                y = vars[command[3]]
            except KeyError: 
                print("undefined")
                continue
            op = command[2]
            if op == "=": op = "=="
            print(str(eval(f"{x}{op}{y}")).lower())
    except EOFError:
        break
