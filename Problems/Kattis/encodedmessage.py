import math
tests = int(input())

for test in range(tests):
    string = input()
    
    width = int(math.pow(len(string),0.5))
    mymatrix = []
    
    for i in range(0,width*width,width):
        mymatrix.append([string[x] for x in list(range(i,i+width))])
    
    rotated = list(zip(*mymatrix[::-1]))
    rotated = list(zip(*rotated[::-1]))
    rotated = list(zip(*rotated[::-1]))

    output = ""
    for row in rotated:
        for letter in row:
            output += letter
    print(output)