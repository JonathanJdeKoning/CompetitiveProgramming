string = input()

if ":)" in string:
    if ":(" in string:
        print("double agent")
    else:
        print("alive")
elif ":(" in string:
    print("undead")
else:
    print("machine")