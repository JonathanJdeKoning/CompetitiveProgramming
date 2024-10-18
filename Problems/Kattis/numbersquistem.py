input()
s = str(eval(input().replace("<]:=","0").replace("/", "//")))
print(s.replace("0","<]:="))