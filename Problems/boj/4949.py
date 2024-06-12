while True:
    s = input()
    if s ==".": break

    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif c in ")}]":
            if not stack: print("no");break
            res = stack.pop()
            if c == ")":
                if res != "(": print("no"); break
            elif c == "}":
                if res != "{": print("no"); break
            elif c == "]":
                if res != "[": print("no"); break
    else:
        if stack:
            print("no")
        else:
            print("yes")
            
        
