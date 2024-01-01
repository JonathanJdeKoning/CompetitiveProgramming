while True:
    
    length = int(input())
    if length == 0:
        break
    x = []
    y = []

    for i in range(length):
        x.append(int(input()))
    for i in range(length):
        y.append(int(input()))
    
    sortedx = sorted(x)
    sortedy = sorted(y)

    newy = []
    for num in x:
        newy.append(str(sortedy[sortedx.index(num)]))
    print("\n".join(newy))
    print()
   