string = input()
idstr = input()
output = ""
x=3 
res=[idstr[y-x:y] for y in range(x, len(idstr)+x,x)]

for num in res:
    output += string[int(num)-1]
print(output)