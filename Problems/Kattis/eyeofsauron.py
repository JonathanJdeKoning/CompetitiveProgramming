string = input()

eye = string.index("(")

if len(string[:eye]) == len(string[eye+2:]):
    print("correct")
else:
    print("fix")