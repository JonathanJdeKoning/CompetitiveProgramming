string = input()
string = string.replace(" ","").lower()
pal = False
for i, c in enumerate(string):
    try:
        strnext = string[i+1]
        if string[i] == strnext:
            pal = True
            break
    except:
        break
    try:
        strforw = string[i+2]
        if string[i] == strforw:
            pal = True
            break
    except:
        continue



print("Palindrome") if pal else print("Anti-palindrome")
