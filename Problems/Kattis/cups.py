tests = int(input())

mylist = []
for i in range(tests):
    yumyum = input().split()
    
    try:
        yumyum[0] = int(yumyum[0])//2
        new = [yumyum[1], yumyum[0]]
        yumyum = new
    except:
        yumyum[1] = int(yumyum[1])
    mylist.append(yumyum)
mylist = sorted(mylist, key=lambda x: x[1])
for thing in mylist:
    print(thing[0])        
    