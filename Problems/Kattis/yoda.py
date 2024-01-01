x = input()
y = input()

loop = min([len(x),len(y)])
x = x[::-1]
y = y[::-1]

newx = ""
newy = ""
for i in range(loop):
    if int(x[i]) > int(y[i]):
        newx+= x[i]
    elif int(x[i]) < int(y[i]):
        newy += y[i]
    else:
        newx += x[i]
        newy += y[i]

newx+=x[loop:]
newy+=y[loop:]
#print(newx)
#print(newy)
        
if newx == "":
    x = "YODA"
    y = int(y[::-1])
elif newy == "":
    y = "YODA"
    x = int(x[::-1])
else:
    y = int(newy[::-1])
    x = int(newx[::-1])
print(x)
print(y)
