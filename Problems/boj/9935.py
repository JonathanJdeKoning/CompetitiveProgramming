s = input()
b = input()

while True:
    old = s
    s = s.replace(b,"")
    if len(old) == len(s): print(s);break
    if not s: print("FRULA");break
