from collections import defaultdict

d = defaultdict(lambda:"UNDECLARED")
for _ in range(int(input())):
    data = input().split()
    if data[0] == "TYPEOF":
        print(d[data[1]])
    elif data[0] == "DECLARE":
        v = data[1]
        typ = data[2]
        if d[v] == "UNDECLARED" or d[v] == typ:
            d[v] = typ
        else:
            print("MULTIPLE DECLARATION")
            break
            
    
