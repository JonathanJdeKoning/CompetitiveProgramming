chars = int(input())

brackets = input()

stack = []
for c in brackets:
    if c in "{([":
        stack.append(c)
    elif c in "})]":
        try:
            top = stack.pop()
        except:
            stack = ["penis"]
            break
        if c == "}" and top != "{":
            break
        elif c == "]" and top != "[":
            break
        elif c == ")" and top != "(":
            break
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")
