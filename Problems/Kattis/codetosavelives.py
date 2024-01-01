tests = int(input())

for i in range(tests):
    x = int(input().replace(" ", ""))
    y = int(input().replace(" ", ""))
    summy = str(x+y)
    
    output = ""
    for c in summy: 
        output += (c + " ")
    print(output[:-1])
    
    