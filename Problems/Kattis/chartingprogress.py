good = True
while True:

    arr = []
    while True:
        try:
            string = input()
        except EOFError:
            good = False
            string = ""
        if string == "":
            break
        else: arr.append(string)

    arr = sorted(list(zip(*arr[::-1])))
    new = list(zip(*arr))
    for line in new[::-1]:
        print("".join(line))
    if good:
        print()
    else:
        break
#list(zip(*original[::-1]))
