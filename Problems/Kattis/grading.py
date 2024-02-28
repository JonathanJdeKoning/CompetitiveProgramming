a,b,c,d,e = list(map(int, input().split()))

grade = int(input())
dun = False
if grade < e and dun == False:
    print("F")
    dun = True
if grade < d and dun == False:
    print("E")
    dun = True
if grade < c and dun == False:
    print("D")
    dun = True
if grade < b and dun == False:
    print("C")
    dun = True
if grade < a and dun == False:
    print("B")
    dun = True
if grade >= a and dun == False:
    print("A")
    
