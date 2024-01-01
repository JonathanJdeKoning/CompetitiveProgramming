tests = int(input())
for _ in range(tests):
    adv = input()

    fail = False
    history = []
    money = 0
    incense = 0
    gems = 0
    curr = None
    for c in adv:
        if c == "$":
            money+=1
            history.append("$")
        elif c == "|":
            incense += 1
            history.append("|")
        elif c == "*":
            gems += 1
            history.append("*")
        elif c == "b":
            try:
                if history[-1] == "$":
                    history = history[:-1]
                    money -= 1
                else:
                    fail = True
                    break
            except:
                fail = True
                break
        elif c == "t":
            try:
                if history[-1] == "|":
                    history = history[:-1]
                    incense -= 1
                else:
                    fail = True
                    break
            except:
                fail = True
                break
        elif c == "j":
            try:
                if history[-1] == "*":
                    history = history[:-1]
                    gems -= 1
                else:
                    fail = True
                    break
            except:
                fail = True
                break
        else:
            continue
    if money != 0 or incense != 0 or gems != 0:
        fail = True
    print("YES") if not fail else print("NO")
